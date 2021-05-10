from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
Year_CHOICES = (
    ('1970','1970'),
    ('1971', '1971'),
    ('1972','1972'),
    ('1973','1973'),
    ('1974','1974'),
    ('1975','1975'),
    ('1976','1976'),
    ('1977','1977'),
    ('1978','1978'),
    ('1979','1979'),
    ('1980','1980'),
    ('1981','1981'),
    ('1982','1982'),
    ('1983','1983'),
    ('1984','1984'),
    ('1985','1985'),
    ('1986','1986'),
    ('1987','1987'),
    ('1988','1988'),
    ('1989','1989'),
    ('1990','1990'),
    ('1991','1991'),
    ('1992','1992'),
    ('1993','1993'),
    ('1994','1994'),
    ('1995','1995'),
    ('1996','1996'),
    ('1997','1997'),
    ('1998','1998'),
    ('1999','1999'),
    ('2000','2000'),
)
class Image(models.Model):
    myid = models.AutoField
    caption=models.CharField(max_length=100)
    name=models.CharField(max_length=6, choices=Year_CHOICES, default='green')
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