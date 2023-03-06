from django.urls import path, re_path

from . import views

urlpatterns = [
    path('posts/<slug:slug>/', views.detailPost, name="detail"),
    path('', views.index),
    # re_path(r'^/blog/post/(?P<slug>[\w-]+)/$', views.detailPost),
    ]