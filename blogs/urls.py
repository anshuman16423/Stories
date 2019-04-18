from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [

    url('^$', views.index),
    url(r'addBlog', views.create_blog),
]