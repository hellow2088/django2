from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$',views.myindex,name = 'myindex'),
    url(r'^mylogin/$',views.mylogin,name='mylogin'),
    url(r'^cgpwd/$',views.cgpwd,name='cgpwd'),
    url(r'^test/$', views.cgpwd, name='cgpwd'),
    url(r'^ajtest/$', views.ajtest, name='ajtest'),
    url(r'^repajax/$', views.repajax, name='repajax'),
    url(r'^get_validCode_img/$', views.get_validCode_img, name='get_validCode_img'),
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),



]
