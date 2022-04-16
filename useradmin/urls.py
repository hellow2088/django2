from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'register$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    # url(r'^login2/$', views.login, name='login2'),
    url(r'^jsif/$', views.jsif, name='jsif'),
    url(r'^edituser/$', views.edituser, name='edituser'),
    url(r'^lf/$', views.login_form, name='login_form'),




]