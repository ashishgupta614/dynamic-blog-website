from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('/postcomment',views.postComment, name='postComment' ),
    path('/createblog',views.createblog, name='createblog' ),
    path('/search',views.search, name='search' ),
    path('',views.bloghome, name='BlogHome' ),
    path('/<str:slug>',views.blogpost, name='Blogpost' ),
]

