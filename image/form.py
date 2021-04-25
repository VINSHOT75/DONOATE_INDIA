from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("caption","reg","hog","hogph","address","state","city","pin","name","phone","ifsc","accno","desc","image","ngo_contact_no")
        labels = {
            'caption':'Name Of Organisation ',
            'reg' : 'License Number ',
            'hog': 'Head Of Organisation ',
            'hogph': 'Mobile No. ',
            'address': 'Address ',
            'state': 'State ',
            'city': 'City ',
            'pin': 'PIN Code ',
            'name': 'Year Of Establishment ',
            'phone': 'NGO Phone No. ',
            'ifsc': 'IFSC Code ',
            'accno': 'Account Number ',
            'image': 'NGO Display Picture ',
            'desc': 'Description',
            'ngo_contact_no': 'NGO Contact No'
        }