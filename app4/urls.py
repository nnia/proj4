#from django.contrib import admin
#from django.urls import include, path

#urlpatterns = [
#    path('app4/', include('app4.urls')),
#   path('admin/', admin.site.urls),
#


from django.conf.urls import include, url

from . import views
#from django.conf.urls import url
#from . import views

app_name = 'app4'

urlpatterns = [
#    url(r'^$', views.index, name='index'),
#    url(r'^$', views.index, name='index'),
    url(r'^coding.html$', views.coding, name='coding'),
    url(r'^contact.html$', views.contact, name='contact'),    
    url(r'^testbase.html$', views.testbase, name='testbase'),
    url(r'^best_dprk.html$', views.best_dprk, name='best_dprk'),
    url(r'^enfant.html$', views.enfant, name='enfant'),    
    url(r'^answer.html$', views.answer, name='answer'),
    url(r'^defaultf.html$', views.defaultf, name='defaultf'),
    url(r'^current_datetime$', views.current_datetime, name='current_datetime'),
    url(r'', views.index, name='index'),    
]