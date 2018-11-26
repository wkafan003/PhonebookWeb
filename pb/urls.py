from django.conf.urls import url
from django.urls import path, reverse
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('contact/add/', views.contactAdd, name='contactAdd'),
    path('contact/<int:contact_id>/edit', views.contactEdit, name='contactEdit'),
    path('contact/<int:contact_id>/delete', views.contactDelete, name='contactDelete'),

    path('city/', views.city, name='city'),
    path('city/add/', views.cityAdd, name='cityAdd'),
    path('city/delete', views.cityDelete, name='cityDelete'),

    path('street/', views.street, name='street'),
    path('street/add/', views.streetAdd, name='streetAdd'),
    path('street/delete', views.streetDelete, name='streetDelete'),

]
