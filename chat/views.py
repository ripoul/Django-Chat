# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Profile, Message

import string
import random
import datetime


@login_required(login_url='/chat/login/')
def index(request):
    msg = Message.objects.all()
    user = request.user

    context={
        "msg":msg,
        "user":user
    }
    
    return render(request, 'chat/index.html', context)

def loginView(request):
    context = {}
    return render(request, 'chat/login.html', context)


def Connect(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/chat/')
        # Redirect to a success page.
    else:
        context = { "error" : "erreur authentification"}
        return render(request, 'chat/login.html', context)


def disconect(request):
    logout(request)
    return redirect('/chat/login/')


def createUser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']

    try:
        user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
    
        ppstr = handle_uploaded_file(request.FILES['pp'])
        user.first_name=firstname
        user.last_name=lastname
        user.profile.photo=ppstr
        user.save()

        login(request, user)
        return redirect('/chat/')

    except:
        context = { "error" : "erreur creation profile"}
        return render(request, 'chat/login.html', context)


def handle_uploaded_file(f):
    title = 'chat/static/pp/'+id_generator()+'.jpeg'
    with open(title, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        
    return title


def id_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required(login_url='/chat/login/')
def sendMessage(request):
    if request.method == 'POST':
        msg = request.POST['msg']
        pub_date = datetime.datetime.now()
        user = request.user

        profile = Profile.objects.get(user=user)

        objMessage = Message(msg=msg, pub_date=pub_date, user=profile)
        objMessage.save()

    return redirect('/chat/')

@login_required(login_url='/chat/login/')
def deleteMessage(request):
    #check if you have the right to delete the msg
    if request.method == 'GET':
        id = request.GET['msgID']
        Message.objects.get(pk=id).delete()
    return redirect('/chat/')