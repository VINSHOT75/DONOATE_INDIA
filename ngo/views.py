from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages


def home(request):
    return render(request,'ngo/home.html')

def logmein(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username , password = password)
        print(password)
        if user is not None:
            auth.login(request,user)
            return redirect('../feed/')
        else:
            print('invalid')
    return render(request,'ngo/login.html')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if len(username)>10:
            print("chota username dalo")
            return redirect('signup')
        if len(password)<8:
            print("bada password daal le gandmareeeee")
            return redirect('signup')

        if not username.isalnum():
            print("dollar mat likh")
            return redirect('signup')

        if password != password1:
            print("password doesnt match")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            print('sorry')
        else:
            user = User.objects.create_user( username = username, first_name = first_name,last_name = last_name , email=email , password = password)
            user.save()
            return redirect('login')

        messages.success(request,"You Signed Up Successfully !! , Now you can log in ..")



    return render(request,'ngo/nsignup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')