from . import views
from django.urls import path

urlpatterns=[

path('getmessage/',views.getmessage,name='getmessage'),

]