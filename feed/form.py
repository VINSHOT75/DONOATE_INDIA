from django import forms
from django.db.models import fields
from .models import Postimg
class ImageForm(forms.ModelForm):
    class Meta:
        model=Postimg
        fields=("caption","image")


