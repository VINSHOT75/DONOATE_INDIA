from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.EmailField()
    subject = models.CharField(max_length=50,default="")
    message = models.CharField(max_length=250,default="")
     
    def __str__(self) :
        return self.name