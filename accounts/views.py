import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import userRegistration

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        brokerUserId = request.POST['brokerUserId']
        brokerPwd = request.POST['brokerPwd']
        brokerSecretKey = request.POST['brokerSecretKey']
        brokerAppId = request.POST['brokerAppId']
        brokerTwoFA = request.POST['brokerTwoFA']

        if userRegistration.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return redirect('register')
        elif userRegistration.objects.filter(email=email).exists():
            messages.info(request, 'Email alreay registered')
            return redirect('register')
        else:
            user = userRegistration.objects.create(username=username, password=password1, email=email, fname=first_name, lname=last_name, brokerUserId = brokerUserId, brokerPwd = brokerPwd, brokerSecretKey = brokerSecretKey, brokerAppId = brokerAppId, brokerTwoFA = brokerTwoFA)
            user.save()
            userAuth = User.objects.create_user(username=username, password=password1)
            userAuth.save()
            return redirect('login')
    else:
        return render(request, 'register.html')

###Login###
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

###Logout###
def logout(request):
    auth.logout(request)
    return redirect('/')
