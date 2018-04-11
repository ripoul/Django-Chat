# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Profile, Message, Room

import string
import random
import datetime


@login_required(login_url='/chat/login/')
def room(request, roomID):
    try:
        roomObj = Room.objects.get(id=roomID)
    except:
        return redirect('/chat/selectRoom')

    user = request.user
    profile = Profile.objects.get(user=user)

    roomsAcces = Room.objects.filter(user=profile)

    if not roomObj in roomsAcces:
        return redirect('/chat/selectRoom')

    msg = Message.objects.filter(room=roomObj)
    user = request.user

    context={
        "msg":msg,
        "user":user,
        "room":roomObj
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
        return redirect('/chat/selectRoom')
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
        return redirect('/chat/selectRoom')

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
        roomID = request.POST['room']
        pub_date = datetime.datetime.now()
        user = request.user

        profile = Profile.objects.get(user=user)

        roomObj = Room.objects.get(id=roomID)

        objMessage = Message(msg=msg, pub_date=pub_date, user=profile, room=roomObj)
        objMessage.save()

    return redirect('/chat/room/'+str(roomID))

@login_required(login_url='/chat/login/')
def deleteMessage(request):
    #check if you have the right to delete the msg
    if request.method == 'GET':
        id = request.GET['msgID']
        roomID= request.GET['roomID']
        Message.objects.get(pk=id).delete()
    return redirect('/chat/room/'+str(roomID))


@login_required(login_url='/chat/login/')
def selectRoom(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    room = Room.objects.filter(user=profile)

    context = { "room" : room}
    return render(request, 'chat/selectRoom.html', context)


@login_required(login_url="/chat/login/")
def createRoomForm(request):
    profile = Profile.objects.all()

    context = { "profiles" : profile}
    return render(request, 'chat/createRoomForm.html', context)

@login_required(login_url="/chat/login/")
def createRoom(request):
    if request.method == 'POST':
        name = request.POST['name']
        users = request.POST.getlist('user')

        RoomObj = Room(name=name)
        RoomObj.save()

        for user in users:
            #add user to the 
            profile = Profile.objects.get(id=user)
            RoomObj.user.add(profile)
        
        RoomObj.save()

    return redirect('/chat/selectRoom/')

@login_required(login_url="/chat/login/")
def joinRoom(request):
    if request.method == 'POST':
        idRoom = request.POST['room']
        roomObj = Room.objects.get(id=idRoom)

        user = request.user
        profile = Profile.objects.get(user=user)

        roomsAcces = Room.objects.filter(user=profile)

        if roomObj in roomsAcces:
            return redirect('/chat/room/'+str(roomObj.id))

        return redirect('/chat/selectRoom/')

    return redirect('/chat/selectRoom/')
