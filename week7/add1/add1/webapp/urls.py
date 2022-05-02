from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .views import insert,display,update_view,delete_view

urlpatterns = [
    url(r'^insert/',insert,name="insert"),
    path('display/',display,name="display"),
    path('delete/<id>',delete_view,name="delete"),
    path('update/<id>',update_view,name="update")
]
