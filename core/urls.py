from django.urls import path

# from . import views
from . import example_views

urlpatterns=[
    # path('getmessage/',views.getmessage,name='getmessage'),
    path('hook/', example_views.hook, name='hook'),
]