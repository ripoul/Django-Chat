from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views




urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.loginView, name='loginView'),
    url(r'^connect/$', views.Connect, name='connect'),
    url(r'^disconect/$', views.disconect, name='disconect'),
    url(r'^createUser/$', views.createUser, name='createUser'),
    url(r'^sendMessage/$', views.sendMessage, name='sendMessage'),
]