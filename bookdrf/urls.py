from django.conf.urls import url

from . import views_Mixin

urlpatterns = [
    url(r'^books$', views_Mixin.BooksView.as_view()),  # 增，查
    url(r'^books_get/(?P<pk>\d+)$', views_Mixin.BooksView.as_view()),   #查，改，删除
    url(r'^vuetest/$', views_Mixin.vuetest, name='vuetest'),

    url(r'^org$', views_Mixin.OrganizationView.as_view()),
    url(r'^org/(?P<pk>\d+)$', views_Mixin.OrganizationView.as_view()),
    url(r'^hero$', views_Mixin.HeroView.as_view()),
    url(r'^hero/(?P<pk>\d+)$', views_Mixin.HeroView.as_view()),
]
