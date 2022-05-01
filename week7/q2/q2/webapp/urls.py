from django.conf.urls import include,url 
from webapp.views import insert,display

urlpatterns = [ 
 url(r'^insert/', insert, name='insert'),
 url(r'^display/', display, name='display'), 
 ] 
