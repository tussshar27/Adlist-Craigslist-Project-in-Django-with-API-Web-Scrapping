from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new_search', views.new_search, name="new_search"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
]
