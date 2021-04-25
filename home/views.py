from django.shortcuts import render
from . models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name",'')
        email = request.POST.get("email",'')
        subject = request.POST.get("name",'')
        message = request.POST.get("name",'')
        cont = Contact(name = name , email = email , subject = subject , message = message)
        cont.save()
        messages.success(request,"Your Form is submitted successfully , we will contact u soon!!!")
    return render(request,"home/contact.html")