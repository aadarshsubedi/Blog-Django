from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("Blog/",views.blog,name='blog'),
    path("category/",views.category,name='category'),
    path("contact/",views.contact,name='contact'),
    path("single/",views.single,name='single')
    
]