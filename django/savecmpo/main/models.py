import datetime
from django.utils import timezone
from django.db import models
from django.db.models.fields.related import ForeignKey
from PIL import Image

# Create your models here.

class Duty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cchangwat(models.Model):
    changwatcode = models.CharField(max_length=2)
    changwatname = models.CharField(max_length=155)
    zonecode = models.CharField(max_length=2)
    changwatname_en = models.CharField(max_length=155)

    def __str__(self):
        return self.changwatname

class Campur(models.Model):
    ampurcode = models.CharField(max_length=2)
    ampurname = models.CharField(max_length=155)
    ampurcodefull = models.IntegerField()
    changwatcode = models.ForeignKey(Cchangwat, on_delete=models.CASCADE)

    def __str__(self):
        return self.ampurname

class Ctambon(models.Model):
    tamboncode = models.CharField(max_length=2)
    tambonname = models.CharField(max_length=155)
    tamboncodefull = models.CharField(max_length=6)
    ampurcode = models.ForeignKey(Campur, on_delete=models.CASCADE)
    changwatcode = models.ForeignKey(Cchangwat, on_delete=models.CASCADE)

    def __str__(self):
        return self.tambonname

class Savecmpo(models.Model):
    sex = (
        ('1','ชาย'),
        ('2','หญิง'),
    )

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=sex, default='ชาย')
    age = models.IntegerField()
    id_card = models.CharField(max_length=15)
    mobile_phone = models.CharField(max_length=10)
    mobile_partner = models.CharField(max_length=10, null=True, blank=True)
    date_arrive = models.DateField(default=datetime.date.today)
    date_leave = models.DateField(default=datetime.date.today)
    Cchangwat = models.ForeignKey(Cchangwat, on_delete=models.CASCADE)
    campur = models.ForeignKey(Campur, on_delete=models.CASCADE)
    ctambon = models.ForeignKey(Ctambon, on_delete=models.CASCADE)
    moo = models.CharField(max_length=255, null=True, blank=True)
    house = models.CharField(max_length=255)
    duty = models.ForeignKey(Duty, on_delete=models.CASCADE)
    vaccine_pic = models.ImageField(upload_to ='vaccine_pic/', blank=True)
    sickness = models.ImageField(upload_to ='sickness/', blank=True)
    lab = models.ImageField(upload_to='lab/', blank=True)
    input_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Savecmpo, self).save(*args, **kwargs)

    def __str__(self):
        return self.fname+' - '+self.lname+' - '+self.id_card