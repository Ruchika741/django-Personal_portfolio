# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name='blog' # In case you have multiple details for different apps

urlpatterns = [
   
    path('',views.all_blogs, name='all_blogs'),
    #path('Hello/',views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/',views.detail, name='detail'),#int values will go inside blog_id variable
   
]


