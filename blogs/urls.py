from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [

    url('^$', views.index),
    url(r'addBlog', views.create_blog),
    url(r'/show/(?P<blog_id>[0-9]+)/$', views.show_blog, name='blog_id'),
]