from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='Home' ),
    path('contact',views.contact, name='Contact' ),
    path('about',views.about, name='About Us' ),
    #path('search',views.search, name='Search' ),
    path('signup',views.handleSignup, name='handleSignup' ),
    path('login',views.handleLogin, name='handleLogin' ),
    path('logout',views.handleLogout, name='handleLogout' ),
]
