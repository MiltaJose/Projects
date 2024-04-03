from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import redirect
# Create your views here.
def register(request):
    if request.method =='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"mail id exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save();
                return redirect('login')
                #print("user created")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')

    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
