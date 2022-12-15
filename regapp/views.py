from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def regg(request):
    if request.method=='POST':
        un = request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        e = request.POST['email']
        p = request.POST['password']
        cp = request.POST['password1']
        if p==cp:
            if User.objects.filter(username=un).exists():
                messages.info(request,"username already exist")
                return redirect ('regg')
            elif User.objects.filter(email=e).exists():
                messages.info(request,"email id already exist")
                return redirect ('regg')
            else:
                user=User.objects.create_user(username=un,first_name=fn,last_name=ln,email=e,password=p)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect ('regg')

    return render(request, "register.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')