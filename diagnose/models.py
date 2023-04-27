from django.db import models


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    dob = models.DateField()
    bgroup = models.CharField(max_length=5)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    join = models.DateTimeField()


class Doctor(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    spec = models.CharField(max_length=20)
    exper = models.IntegerField()
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    join = models.DateTimeField()


class Admin(models.Model):
    adid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=15)
    scode = models.IntegerField()
    join = models.DateTimeField()


class History(models.Model):
    hid = models.AutoField(primary_key=True)
    hdate = models.DateField()
    htime = models.TimeField()
    uname = models.CharField(max_length=30)
    uemail = models.CharField(max_length=50)
    dname = models.CharField(max_length=30)
    dphone = models.IntegerField()
    demail = models.CharField(max_length=50)
    dspec = models.CharField(max_length=20)
    daddress = models.CharField(max_length=100)
    sym1 = models.CharField(max_length=30)
    sym2 = models.CharField(max_length=30)
    sym3 = models.CharField(max_length=30)
    sym4 = models.CharField(max_length=30)
    sym5 = models.CharField(max_length=30)
    disease = models.CharField(max_length=30)


class Appoint(models.Model):
    apid = models.AutoField(primary_key=True)
    date = models.DateField()
    time = models.TimeField()
    uname = models.CharField(max_length=30)
    uemail = models.CharField(max_length=50)
    dname = models.CharField(max_length=30)
    dphone = models.IntegerField()
    demail = models.CharField(max_length=50)
    dspec = models.CharField(max_length=20)
    daddress = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

class Feed(models.Model):
    fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=250)