from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_blog_list, name='my_blog_list'),
    path('create/', views.blog_create, name='blog_create'),
]