from django.conf.urls import url
from . import views

urlpatterns = [
 
 url(r'^login/', views.page1,name = 'login'),
 
]
