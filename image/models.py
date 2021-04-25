from django.db import models

# Create your models here.
class Image(models.Model):
    myid = models.AutoField
    caption=models.CharField(max_length=100)
    name=models.CharField(max_length=100,default="")
    org=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=100,default="")
    phone=models.CharField(max_length=100,default="")
    state=models.CharField(max_length=100,default="")
    city=models.CharField(max_length=100,default="")
    pin=models.IntegerField(default="")
    hog=models.CharField(max_length=100,default="")
    reg=models.CharField(max_length=100,default="")
    hogph=models.CharField(max_length=100,default="")
    ifsc=models.CharField(max_length=100,default="")
    accno=models.CharField(max_length=100,default="")
    image=models.ImageField(upload_to="img/%y")
    desc=models.TextField(max_length=200,default="")
    ngo_contact_no=models.CharField(max_length=12,default="")
    def __str__(self):
        return self.caption