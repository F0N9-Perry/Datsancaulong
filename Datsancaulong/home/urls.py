from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('lichdatsan/', views.lichdatsan, name="lichdatsan"),
    path('edit-lichdatsan/', views.edit_lichdatsan, name="edit-lichdatsan")

]