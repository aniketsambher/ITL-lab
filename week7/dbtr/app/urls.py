from django.urls import path
from . import views
urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', views.index,name="index"),
    path('vote',views.vote,name="vote"),
    path('result',views.display,name="display")
]

