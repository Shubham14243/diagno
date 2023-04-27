from django.shortcuts import render
from .models import User, Doctor, Appoint, History, Admin, Feed
from django.contrib import messages
from datetime import date, datetime
from .disease_prediction import RandomForest
from django.core.mail import send_mail
import random


# Create your views here.

def udet(email):
    userdata = User.objects.get(email=email)
    doctor = Doctor.objects.all()
    if Appoint.objects.filter(uemail__exact=email):
        appoint = Appoint.objects.all().filter(uemail__exact=email).order_by('apid').reverse()
    else:
        appoint = Appoint.objects.filter(uemail__exact=email)
    if History.objects.filter(uemail__exact=email):
        report = History.objects.filter(uemail__exact=email).order_by('-hid')[0]
        history = History.objects.all().filter(uemail__exact=email).order_by('hid').reverse()
    else:
        report = History.objects.filter(uemail__exact=email)
        history = History.objects.all().filter(uemail__exact=email)
    dat = [userdata, doctor, appoint, history, report]
    return dat


def ddet(email):
    docdata = Doctor.objects.get(email=email)
    if Appoint.objects.filter(demail__exact=email):
        appoint = Appoint.objects.all().filter(demail__exact=email).order_by('apid').reverse()
    else:
        appoint = Appoint.objects.filter(demail__exact=email)
    if History.objects.filter(uemail__exact=email):
        patient = History.objects.all().filter(demail__exact=email).order_by('hid').reverse()
    else:
        patient = History.objects.filter(demail__exact=email)
    dat = [docdata, patient, appoint]
    return dat

def admdet(email):
    admdata = Admin.objects.get(email=email)
    appoint = Appoint.objects.all().order_by('apid').reverse()
    patdata = User.objects.all().order_by('uid').reverse()
    docdata = Doctor.objects.all().order_by('did').reverse()
    fdata = Feed.objects.all().order_by('fid').reverse()
    dat = [admdata, appoint, patdata, docdata, fdata]
    return dat

def homedata():
    docdata = Doctor.objects.order_by('-did')
    dlist = []
    for i in range(4):
        dlist.append(docdata[i])
    fed = Feed.objects.order_by('-fid')
    flist = []
    for i in range(3):
        flist.append(fed[i])
    return dlist,flist

def home(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html', {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        dlst, flst = homedata()
        return render(request, 'index.html', {'docd':dlst, 'feed': flst})


def admlog(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'admin.html')


def log(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'login.html')


def reg(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'register.html')


def doc(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        docdata = Doctor.objects.all()
        return render(request, 'doctors.html', {'doc': docdata})


def doclog(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'doclogin.html')


def docreg(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'docregister.html')


def udash(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'login.html')


def ddash(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'doclogin.html')


def adash(request):
    if 'user' in request.session:
        email = request.session['user']
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'dashadmin.html')


def result(request):
    if 'user' in request.session:
        return render(request, 'result.html')
    elif 'doc' in request.session:
        email = request.session['doc']
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
    elif 'admin' in request.session:
        email = request.session['admin']
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
    else:
        return render(request, 'login.html')


def ures(request):
    if request.method == 'POST':

        em = request.POST["remail"]
        ph = request.POST["rphone"]
        dob = request.POST["rdob"]

        if User.objects.filter(email__exact=em, phone__exact=ph, dob__exact=dob):
            messages.success(request, 'Account Verified! Enter New Password!')
            return render(request, 'resetuserpass.html', {'em':em})
        else:
            messages.error(request, 'User Not Found!')
            return render(request, 'login.html')


def resetuser(request):
    if request.method == 'POST':

        em = request.POST["email"]
        np = request.POST["npass"]
        cp = request.POST["cpass"]

        if np == cp:
            if User.objects.filter(email__exact=em).update(password=cp):
                messages.success(request, 'Password Updated! Please Login!')
            else:
                messages.error(request, 'Error Occured! Please Try Again!')
        else:
            messages.error(request, 'Password Not Matched! Try Again!')
        return render(request, 'login.html')


def dres(request):
    if request.method == 'POST':

        em = request.POST["remail"]
        ph = request.POST["rphone"]

        if Doctor.objects.filter(email__exact=em, phone__exact=ph):
            messages.success(request, 'Account Verified! Enter New Password!')
            return render(request, 'resetdocpass.html', {'em':em})
        else:
            messages.error(request, 'User Not Found!')
            return render(request, 'doclogin.html')


def resetdoc(request):
    if request.method == 'POST':

        em = request.POST["demail"]
        np = request.POST["npass"]
        cp = request.POST["cpass"]

        if np == cp:
            if Doctor.objects.filter(email__exact=em).update(password=cp):
                messages.success(request, 'Password Updated! Please Login!')
            else:
                messages.error(request, 'Error Occured! Please Try Again!')
        else:
            messages.error(request, 'Password Not Matched! Try Again!')
        return render(request, 'doclogin.html')

def ares(request):
    if request.method == 'POST':

        em = request.POST["remail"]
        ph = request.POST["scode"]

        if Admin.objects.filter(email__exact=em, scode__exact=ph):
            messages.success(request, 'Account Verified! Enter New Password!')
            return render(request, 'resetadminpass.html', {'em': em})
        else:
            messages.error(request, 'User Not Found!')
            return render(request, 'admin.html')


def resetadm(request):
    if request.method == 'POST':

        em = request.POST["ademail"]
        np = request.POST["npass"]
        cp = request.POST["cpass"]

        if np == cp:
            if Admin.objects.filter(email__exact=em).update(password=cp):
                messages.success(request, 'Password Updated! Please Login!')
            else:
                messages.error(request, 'Error Occured! Please Try Again!')
        else:
            messages.error(request, 'Password Not Matched! Try Again!')
        return render(request, 'admin.html')


def otp_varify(request):
    if request.method == 'POST':
        eotp = request.POST["otp"]
        type = request.POST["type"]
        gotp = request.POST["gotp"]
        email = request.POST["mail"]

        if gotp == eotp:
            messages.success(request, "Logged In Successfully!")
            if type == 'user':
                request.session['user'] = email
                data = udet(email)
                return render(request, 'dashuser.html', {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
            elif type == 'doc':
                request.session['doc'] = email
                data = ddet(email)
                return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
            elif type == 'admin':
                request.session['admin'] = email
                data = admdet(email)
                return render(request, 'dashadmin.html', {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
        else:
            messages.success(request, 'OTP Verification Failed!')
            return render(request, 'otpverify.html', {'umail': email, 'type': type})


def register_user(request):
    if request.method == 'POST':
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        dob = request.POST["dob"]
        bgroup = request.POST["bgroup"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        address = request.POST["address"]
        joindate = datetime.now()
        if password == confirm:
            var = User.objects.filter(email__exact=email).exists()
            if var is True:
                messages.warning(request, 'User Already Registered!')
                return render(request, 'register.html')
            else:
                data = User(name=name, phone=phone, email=email, dob=dob, bgroup=bgroup, gender=gender,
                            password=password, address=address, join=joindate)
                data.save()
                otp = random.randint(000000, 999999)
                message = "Thanks for chosing Diagno for Health Diagnosis.\nPlease refer to the OTP for Login/Registration purpose.\n OTP = " + str(
                    otp) + "\nThank You\nAdmin\nDiagno - Health Prediction"
                sendemail = send_mail('Verify OTP', message, 'Diagno - Health Diagnosis', [email], fail_silently=True)
                if sendemail:
                    messages.success(request, 'Registered! OTP sent to Email Successfully!')
                    return render(request, 'otpverify.html', {'umail': email, 'type': 'user', 'gotp': otp})
                else:
                    messages.error(request, 'Failed to Send OTP! Try Again!')
                    return render(request, 'register.html')
        else:
            messages.error(request, 'Password & Confirm Password Not Matched!!!')
            return render(request, 'register.html')
    else:
        messages.error(request, 'Error Occurred! Get-Started Again!!!')
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        var = User.objects.filter(email__exact=email, password__exact=password).exists()
        if var is True:
            otp = random.randint(000000,999999)
            message = "Thanks for chosing Diagno for Health Diagnosis.\nPlease refer to the OTP for Login/Registration purpose.\n OTP = "+str(otp)+"\nThank You\nAdmin\nDiagno - Health Prediction"
            sendemail = send_mail('Verify OTP',message,'Diagno - Health Diagnosis',[email],fail_silently=False)
            if sendemail:
                messages.success(request, 'OTP sent to Email Successfully!')
                return render(request, 'otpverify.html', {'umail': email, 'type': 'user', 'gotp':otp})
            else:
                messages.error(request, 'Failed to Send OTP! Try Again!')
                return render(request, 'login.html')
        else:
            messages.warning(request, 'Invalid Login Credentials!!!')
            return render(request, 'login.html')
    else:
        messages.error(request, 'Error Occurred! Login Again!!!')
        return render(request, 'login.html')


def logout(request):
    del request.session['user']
    messages.success(request, 'Successfully Logged Out!')
    return render(request, 'login.html')


def diag(request):
    dislist = []
    email = request.session['user']
    if request.method == 'POST':
        sym1 = request.POST["s1"]
        sym2 = request.POST["s2"]
        sym3 = request.POST["s3"]
        sym4 = request.POST["s4"]
        sym5 = request.POST["s5"]

        if sym1 != "":
            dislist.append(sym1)

        if sym2 != "":
            dislist.append(sym2)

        if sym3 != "":
            dislist.append(sym3)

        if sym4 != "":
            dislist.append(sym4)

        if sym5 != "":
            dislist.append(sym5)

        today = date.today()
        hdate = today.strftime("%Y-%m-%d")
        now = datetime.now()
        htime = now.strftime("%H:%M:%S")
        udat = User.objects.get(email=email)
        uname = udat.name
        uemail = email

        if sym3 == "" and sym4 == "" and sym5 == "":
            messages.error(request, 'Your Symptoms are not Severe! Take Some Rest and Further Diagnose Again!')
        if sym1 == "dry_cough" and sym2 == "fever" and sym3 == "difficulty_in_breathing" and sym4 == "loss_of_smell_and_taste" and sym5 == "headache":
            disease = "Covid19"
            dd = Doctor.objects.get(spec=disease)
            dname = dd.name
            dphone = dd.phone
            demail = dd.email
            dspec = dd.spec
            daddress = dd.address

            data = History(hdate=hdate, htime=htime, uname=uname, uemail=uemail, dname=dname, dphone=dphone,
                           demail=demail, dspec=dspec, daddress=daddress, sym1=sym1, sym2=sym2, sym3=sym3, sym4=sym4,
                           sym5=sym5, disease=disease)
            data.save()
            userdata = User.objects.get(email=email)
            return render(request, 'result.html', {'dlist': dislist, 'udat': userdata, 'dis': disease, 'doc': dd})
        else:
            disease = RandomForest(dislist)
            dd = Doctor.objects.get(spec=disease)
            dname = dd.name
            dphone = dd.phone
            demail = dd.email
            dspec = dd.spec
            daddress = dd.address

            data = History(hdate=hdate, htime=htime, uname=uname, uemail=uemail, dname=dname, dphone=dphone,
                           demail=demail, dspec=dspec, daddress=daddress, sym1=sym1, sym2=sym2, sym3=sym3, sym4=sym4,
                           sym5=sym5, disease=disease)
            data.save()
            userdata = User.objects.get(email=email)
            return render(request, 'result.html', {'dlist': dislist, 'udat': userdata, 'dis': disease, 'doc': dd})

    else:
        messages.error(request, 'Error Occurred! Diagnose Again!!!')
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})


def appt(request):
    if request.method == 'POST':
        apdate = request.POST["adate"]
        aptime = request.POST["atime"]
        uname = request.POST["unme"]
        uemail = request.POST["ueml"]
        dname = request.POST["dname"]
        dphone = request.POST["dphone"]
        demail = request.POST["demail"]
        dspec = request.POST["dspec"]
        daddress = request.POST["daddress"]

        status = "Pending"

        aptsave = Appoint(date=apdate, time=aptime, uname=uname, uemail=uemail, dname=dname, dphone=dphone,
                          demail=demail, dspec=dspec, daddress=daddress, status=status)
        aptsave.save()

        email = request.session['user']
        messages.success(request, 'Appointment Booked Successfully!')
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})


def delapp(request):
    if request.method == 'POST':
        apid = request.POST["apid"]

        delap = Appoint.objects.get(apid=apid).delete()
        if delap:
            email = request.session['user']
            messages.success(request, 'Appointment Cancelled Successfully!')
            data = udet(email)
            return render(request, 'dashuser.html',
                          {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})


def updapp(request):
    if request.method == 'POST':
        apid = request.POST["apid"]
        apdate = request.POST["apdate"]
        aptime = request.POST["aptime"]

        updap = Appoint.objects.filter(apid__exact=apid).update(date=apdate, time=aptime)
        if updap:
            email = request.session['user']
            messages.success(request, 'Appointment Updated Successfully!')
            data = udet(email)
            return render(request, 'dashuser.html',
                          {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})


def updpro(request):
    if request.method == 'POST':
        name = request.POST["uname"]
        phone = request.POST["uphone"]
        email = request.session['user']
        dob = request.POST["udob"]
        bld = request.POST["ubld"]
        add = request.POST["uadd"]

        updpr = User.objects.filter(email__exact=email).update(name=name, phone=phone, dob=dob, bgroup=bld, address=add)
        if updpr:
            messages.success(request, 'Profile Updated Successfully!')
            data = udet(email)
            return render(request, 'dashuser.html',
                          {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})


def updpass(request):
    if request.method == 'POST':
        cur = request.POST["curpass"]
        new = request.POST["newpass"]
        con = request.POST['repass']

        email = request.session['user']
        updpa = User.objects.get(email=email)
        if updpa.password == cur and con == new:
            updpas = User.objects.filter(email__exact=email).update(password=con)
            if updpas:
                messages.success(request, 'Password Updated Successfully! Please Login Again!')
                return render(request, 'login.html')
            else:
                messages.success(request, 'Error Occured! Try Again!')
        else:
            messages.success(request, 'Current Password Not Matched!')
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})


def dellpro(request):
    if request.method == 'POST':
        pasd = request.POST["delpass"]
        email = request.session['user']
        updpa = User.objects.get(email=email)
        if updpa.password == pasd:
            dpas = User.objects.filter(email__exact=email, password__exact=pasd).delete()
            if dpas:
                del request.session['user']
                messages.success(request, 'Account Deleted Successfully!')
                return render(request, 'login.html')
            else:
                messages.success(request, 'Error Occured! Try Again!')
        else:
            messages.success(request, 'Password Not Matched!')
        data = udet(email)
        return render(request, 'dashuser.html',
                      {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})


def register_doctor(request):
    if request.method == 'POST':
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        spec = request.POST["docspec"]
        exp = request.POST["docexp"]
        password = request.POST["password"]
        confirm = request.POST["confirm"]
        address = request.POST["address"]
        joindate = datetime.now()
        if password == confirm:
            var = Doctor.objects.filter(email__exact=email).exists()
            if var is True:
                messages.warning(request, 'Doctor Already Registered!')
                return render(request, 'docregister.html')
            else:
                data = Doctor(name=name, phone=phone, email=email, spec=spec, exper=exp, gender=gender,
                            password=password, address=address, join=joindate)
                data.save()
                otp = random.randint(000000, 999999)
                message = "Thanks for chosing Diagno for Health Diagnosis.\nPlease refer to the OTP for Login/Registration purpose.\n OTP = " + str(
                    otp) + "\nThank You\nAdmin\nDiagno - Health Prediction"
                sendemail = send_mail('Verify OTP', message, 'Diagno - Health Diagnosis', [email], fail_silently=True)
                if sendemail:
                    messages.success(request, 'Registered! OTP sent to Email Successfully!')
                    return render(request, 'otpverify.html', {'umail': email, 'type': 'doc', 'gotp': otp})
                else:
                    messages.error(request, 'Failed to Send OTP! Try Again!')
                    return render(request, 'doclogin.html')
        else:
            messages.error(request, 'Password & Confirm Password Not Matched!!!')
            return render(request, 'docregister.html')
    else:
        messages.error(request, 'Error Occurred! Get-Started Again!!!')
        return render(request, 'docregister.html')


def login_doctor(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        var = Doctor.objects.filter(email__exact=email, password__exact=password).exists()
        if var is True:
            otp = random.randint(000000, 999999)
            message = "Thanks for chosing Diagno for Health Diagnosis.\nPlease refer to the OTP for Login/Registration purpose.\n OTP = " + str(
                otp) + "\nThank You\nAdmin\nDiagno - Health Prediction"
            sendemail = send_mail('Verify OTP', message, 'Diagno - Health Diagnosis', [email], fail_silently=True)
            if sendemail:
                messages.success(request, 'OTP sent to Email Successfully!')
                return render(request, 'otpverify.html', {'umail': email, 'type': 'doc', 'gotp': otp})
            else:
                messages.error(request, 'Failed to Send OTP! Try Again!')
                return render(request, 'doclogin.html')
        else:
            messages.warning(request, 'Invalid Login Credentials!!!')
            return render(request, 'doclogin.html')
    else:
        messages.error(request, 'Error Occurred! Login Again!!!')
        return render(request, 'doclogin.html')


def doclogout(request):
    del request.session['doc']
    messages.success(request, 'Successfully Logged Out!')
    return render(request, 'doclogin.html')


def upddocpro(request):
    if request.method == 'POST':
        name = request.POST["uname"]
        phone = request.POST["uphone"]
        email = request.session['doc']
        spec = request.POST["dspec"]
        exp = request.POST["dexp"]
        add = request.POST["uadd"]

        updpr = Doctor.objects.filter(email__exact=email).update(name=name, phone=phone, spec=spec, exper=exp, address=add)
        if updpr:
            messages.success(request, 'Profile Updated Successfully!')
        else:
            messages.error(request, 'Profile Not Updated!')
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})


def upddocpass(request):
    if request.method == 'POST':
        cur = request.POST["curpass"]
        new = request.POST["newpass"]
        con = request.POST['repass']

        email = request.session['doc']
        updpa = Doctor.objects.get(email=email)
        if updpa.password == cur and con == new:
            updpas = Doctor.objects.filter(email__exact=email).update(password=con)
            if updpas:
                messages.success(request, 'Password Updated Successfully! Please Login Again!')
                return render(request, 'doclogin.html')
            else:
                messages.success(request, 'Error Occured! Try Again!')
        else:
            messages.success(request, 'Current Password Not Matched!')
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})


def delldocpro(request):
    if request.method == 'POST':
        pasd = request.POST["delpass"]
        email = request.session['doc']
        updpa = Doctor.objects.get(email=email)
        if updpa.password == pasd:
            dpas = Doctor.objects.filter(email__exact=email, password__exact=pasd).delete()
            if dpas:
                del request.session['doc']
                messages.success(request, 'Account Deleted Successfully!')
                return render(request, 'doclogin.html')
            else:
                messages.success(request, 'Error Occured! Try Again!')
        else:
            messages.success(request, 'Password Not Matched!')
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})


def login_admin(request):
    if request.method == 'POST':
        email = request.POST["ademail"]
        password = request.POST["adpassword"]
        code = request.POST["adcode"]
        var = Admin.objects.filter(email__exact=email, password__exact=password, scode__exact=code).exists()
        if var is True:
            otp = random.randint(000000, 999999)
            message = "Thanks for chosing Diagno for Health Diagnosis.\nPlease refer to the OTP for Login/Registration purpose.\n OTP = " + str(
                otp) + "\nThank You\nAdmin\nDiagno - Health Prediction"
            sendemail = send_mail('Verify OTP', message, 'Diagno - Health Diagnosis', [email], fail_silently=True)
            if sendemail:
                messages.success(request, 'OTP sent to Email Successfully!')
                return render(request, 'otpverify.html', {'umail': email, 'type': 'admin', 'gotp': otp})
            else:
                messages.error(request, 'Failed to Send OTP! Try Again!')
                return render(request, 'admin.html')
        else:
            messages.warning(request, 'Invalid Login Credentials!!!')
            return render(request, 'admin.html')
    else:
        messages.error(request, 'Error Occurred! Login Again!!!')
        return render(request, 'admin.html')


def admlogout(request):
    del request.session['admin']
    messages.success(request, 'Successfully Logged Out!')
    return render(request, 'admin.html')

def updadmpro(request):
    if request.method == 'POST':
        name = request.POST["namead"]
        scode = request.POST["scodead"]
        email = request.session['admin']

        updad = Admin.objects.filter(email__exact=email).update(name=name, scode=scode)
        if updad:
            messages.success(request, 'Profile Updated Successfully!')
        else:
            messages.error(request, 'Profile Not Updated!')
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})


def updadpass(request):
    if request.method == 'POST':
        cur = request.POST["curpass"]
        new = request.POST["newpass"]
        con = request.POST['repass']

        email = request.session['admin']
        updpa = Admin.objects.get(email=email)
        if updpa.password == cur and con == new:
            updadp= Admin.objects.filter(email__exact=email).update(password=con)
            if updadp:
                messages.success(request, 'Password Updated Successfully! Please Login Again!')
                return render(request, 'admin.html')
            else:
                messages.success(request, 'Error Occured! Try Again!')
        else:
            messages.success(request, 'Current Password Not Matched!')
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})


def delladpro(request):
    if request.method == 'POST':
        pasd = request.POST["delpass"]
        email = request.session['admin']
        delac = Admin.objects.get(email=email)
        if delac.password == pasd:
            dadac = Admin.objects.filter(email__exact=email, password__exact=pasd).delete()
            if dadac:
                del request.session['admin']
                messages.success(request, 'Account Deleted Successfully!')
                return render(request, 'admin.html')
            else:
                messages.success(request, 'Error Occured! Try Again!')
        else:
            messages.success(request, 'Password Not Matched!')
        data = admdet(email)
        return render(request, 'dashadmin.html',
                      {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})


def approve(request):
    if request.method == 'POST':
        email = request.session['doc']
        ap = request.POST["apid"]
        con = "Confirmed"
        appr = Appoint.objects.get(apid=ap)
        if appr:
            appr = Appoint.objects.filter(apid__exact=ap).update(status=con)
            messages.success(request, 'Appointment Confirmed Successfully!')
        else:
            messages.error(request, 'Appointment Not Confirmed!')
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})

def cancel(request):
    if request.method == 'POST':
        email = request.session['doc']
        ap = request.POST["apid"]
        con = "Cancelled"
        appr = Appoint.objects.get(apid=ap)
        if appr:
            appr = Appoint.objects.filter(apid__exact=ap).update(status=con)
            messages.success(request, 'Appointment Cancelled Successfully!')
        else:
            messages.error(request, 'Appointment Not Cancelled!')
        data = ddet(email)
        return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})


def get_feed(request):
    if request.method == 'POST':
        name = request.POST["fname"]
        phone = request.POST["fphone"]
        email = request.POST["femail"]
        message = request.POST["fmessage"]

        data = Feed(name=name, phone=phone, email=email, message=message)
        data.save()
        messages.success(request, 'Feedback Successfully Submitted!')
        if 'user' in request.session:
            email = request.session['user']
            data = udet(email)
            return render(request, 'dashuser.html',
                          {'data': data[0], 'rep': data[4], 'doc': data[1], 'app': data[2], 'his': data[3]})
        elif 'doc' in request.session:
            email = request.session['doc']
            data = ddet(email)
            return render(request, 'dashdoc.html', {'data': data[0], 'pat': data[1], 'appt': data[2]})
        elif 'admin' in request.session:
            email = request.session['admin']
            data = admdet(email)
            return render(request, 'dashadmin.html',
                          {'data': data[0], 'appt': data[1], 'pat': data[2], 'doc': data[3], 'fdfd': data[4]})
        else:
            dlst, flst = homedata()
            return render(request, 'index.html', {'docd': dlst, 'feed': flst})