from image.models import Image
from django.shortcuts import render
from .form import ImageForm
from .models import Postimg
from django.contrib.auth.decorators import login_required

@login_required(login_url='../ngo/')
def feed(request):
    feeds = Postimg.objects.all()
    return render(request,'feed/feed.html',{'feeds':feeds})

@login_required(login_url='/ngo/')
def donate(request):
    ngos = Image.objects.all()
    return render(request,'feed/ngolist.html',{'ngos':ngos})

@login_required(login_url='/ngo/')
def donateitem(request):
    return render(request,'feed/donateitem.html')

@login_required(login_url='/ngo/')
def viewdetails(request , myid):
    ngos = Image.objects.filter(id=myid)
    return render(request,'feed/ngoview.html',{'ngos':ngos})

@login_required(login_url='/ngo/')
def payment(request):
    return render(request,'feed/payment.html')

@login_required(login_url='/ngo/')
def stationary(request):
    return render(request,'feed/donatestationary.html')

@login_required(login_url='/ngo/')
def food(request):
    return render(request,'feed/donatefood.html')

@login_required(login_url='/ngo/')
def clothes(request):
    return render(request,'feed/donateclothes.html')

@login_required(login_url='/ngo/')
def time(request):
    return render(request,'feed/donatetime.html')

@login_required(login_url='/ngo/')
def blood(request):
    return render(request,'feed/donateblood.html')



@login_required(login_url='/ngo/')
def add_post(request):
        if request.method == "POST":
            form=ImageForm(data=request.POST,files=request.FILES)
            if form.is_valid():
                obj=form.instance
                obj.user = request.user
                form.save()
                return render(request,"feed/addpost.html",{"obj":obj})  
        else:
            form=ImageForm()    
        img=Postimg.objects.all()
        return render(request,"feed/addpost.html",{"img":img,"form":form})





# Create your views here.
