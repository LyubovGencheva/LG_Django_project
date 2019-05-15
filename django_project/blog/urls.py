from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'), #templates refer to the url tags, instead of url-path being hardcoded

]
