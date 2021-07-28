from django.urls import path

from . import views

urlpatterns=[
    path('getmessage/',views.getmessage,name='getmessage'),
]