from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from haystack.views import SearchView


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^showhero/$', views.showhero, name='showhero'),
    url(r'^delhero/$', views.delhero, name='delhero'),
    url(r'^addhero/$', views.addhero, name='addhero'),
    url(r'^edithero/$', views.edithero, name='edithero'),
    # url(r'^heroinfo/<int:hid>', views.show_hero, name='show_hero'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^windowaddbook/$', views.windowaddbook, name='windowaddbook'),
    url(r'^windowaddbook2/$', views.windowaddbook2, name='windowaddbook2'),

    url(r'^showbooks/$', views.showbooks, name='showbooks'),
    url(r'^showbooks2/$', views.showbooks2, name='showbooks2'),
    url(r'^showbooks_pagehandle/$', views.showbooks_pagehandle, name='showbooks_pagehandle'),

    url(r'^delbook/$', views.delbook, name='delbook'),
    url(r'^editbook/(\d*)$', views.editbook, name='editbook'),
    url(r'^modelEditbook/$', views.modelEditbook, name='modelEditbook'),
    url(r'^test/$', views.test, name='test'),
    url(r'^getdata/$', views.getdata, name='getdata'),
    url(r'^bookhero/$', views.bookhero, name='bookhero'),
    url(r'^writer_list/$', views.WriterListView.as_view(), name='writer_list'),

    url(r'^addwriter/$', views.addwriter, name='addwriter'),
    url(r'^editwriter/$', views.editwriter, name='editwriter'),
    url(r'^getwriter/$', views.getwriter, name='getwriter'),
    url(r'^modal_addwriter/$', views.modal_addwriter, name='modal_addwriter'),
    url(r'^window/$', views.window, name='window'),
    url(r'^layout/$', views.layout, name='layout'),
    url(r'^getmsg/$', views.getmsg, name='getmsg'),
    # url(r'^results/$', views.search, name='search'),
    url(r'search/$', SearchView(), name='haystack_search'),
    url(r'lvbooks/$', views.BooklistView.as_view(), name='booklist_view'),
    url(r'^query/$', views.search, name='search',),

    # url(r'^search/', include(('haystack.urls','haystack'),namespace='haystack')),

]
