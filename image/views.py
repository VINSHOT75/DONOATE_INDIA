from django.shortcuts import render
from .form import ImageForm
from .models import Image
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='../ngo/')
def index(request):

    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"feed/addngo.html",{"obj":obj})
    else:
        form=ImageForm()
    img=Image.objects.all()
    return render(request,"feed/addngo.html",{"img":img,"form":form})