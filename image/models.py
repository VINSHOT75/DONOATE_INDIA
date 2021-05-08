from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Image(models.Model):
    myid = models.AutoField
    caption=models.CharField(max_length=100)
    name=models.IntegerField(default="")
    org=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    phone=PhoneNumberField()
    state=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    pin=models.IntegerField(default="")
    hog=models.CharField(max_length=100,default="")
    reg=models.IntegerField(default="")
    hogph=PhoneNumberField()
    ifsc=models.IntegerField(default="")
    accno=models.IntegerField(default="")
    image=models.ImageField(upload_to="img/%y")
    desc=models.TextField(max_length=20000,default="")
    ngo_contact_no=PhoneNumberField()
    def __str__(self):
        return self.caption