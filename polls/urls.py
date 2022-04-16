from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
    url(r'questions',views.questions,name='questions'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name = 'detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name = 'results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name = 'vote'),
    url(r'add_smoke', views.add_smoke, name='add_smoke'),
    url(r'addjs$', views.addjs, name='addjs'),
    url(r'add', views.add_question, name='add'),

]
