from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [
    url(r'^room/(?P<roomID>[0-9]+)/$', views.room, name='room'),
    url(r'^login/$', views.loginView, name='loginView'),
    url(r'^connect/$', views.Connect, name='connect'),
    url(r'^disconect/$', views.disconect, name='disconect'),
    url(r'^createUser/$', views.createUser, name='createUser'),
    url(r'^sendMessage/$', views.sendMessage, name='sendMessage'),
    url(r'^deleteMessage/$', views.deleteMessage, name='deleteMessage'),
    url(r'^selectRoom/$', views.selectRoom, name='selectRoom'),
    url(r'^createRoomForm/$', views.createRoomForm, name='createRoomForm'),
    url(r'^createRoom/$', views.createRoom, name='createRoom'),
    url(r'^joinRoom/$', views.joinRoom, name='joinRoom'),
]