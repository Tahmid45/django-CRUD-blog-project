from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_post, name='addpost'),
    path('edit/<int:id>',views.edit_post, name='editpost'),
    path('delete/<int:id>',views.delete_post, name='deletepost'),
]
