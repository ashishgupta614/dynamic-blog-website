from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib .auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Contact
from blog.models import Post


def index(request):
    return render(request, 'home/home.html')


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        if (len(name) == 0 or len(email)<3 or len(phone)<10 or len(desc)==0):
            messages.error(request, "Please Fill the form correctly to Contact")
        else:
            contact=Contact(name=name, email=email, phone=phone  ,desc=desc)
            contact.save()
            messages.success(request, "Success")
    return render(request, 'home/contact.html')
# Create your views here.


def about(request):
    return render(request, 'home/about.html')



def handleSignup(request):
    if request.method=='POST':
       fname = request.POST['fname']
       lname = request.POST['lname']
       username = request.POST['username']
       email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2 = request.POST['pass2']

       if not username.isalnum():
           messages.error(request, 'Username must be alphanumeric')
           return redirect('Home')
       if pass1 != pass2:
           messages.error(request, 'Password does not match')
           return redirect('Home')

       myuser=User.objects.create_user(username, email, pass1)
       myuser.first_name=fname
       myuser.last_name=lname
       myuser.save()
       messages.success(request, 'Your account sucessfully created')
       return redirect('Home')
    else:
        return HttpResponse('404-user not found')

def handleLogin(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user=authenticate(username=loginusername, password=loginpassword)
        print(user)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged In')
            return redirect('Home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('Home')
    return HttpResponse("cb")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('Home')
