# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required(login_url='/chat/login/')
def index(request):
    context={}
    return render(request, 'chat/index.html', context)
    #return HttpResponse("ici sera le chat")

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
    
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    return HttpResponse("wip")