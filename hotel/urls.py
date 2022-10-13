from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('home', views.home),
    path('login',views.login),
    path('logged_in', views.logged_in),
    path('sign_up',views.sign_up),
    path("signup",views.signup),
    path("forgot",views.forgot),
    path("book/",views.book),
    path("book/booked",views.booked)
]