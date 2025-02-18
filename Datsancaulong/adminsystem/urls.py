from django.contrib import admin
from django.urls import include, path
from .import views


urlpatterns = [
    
    path('adminaccount/', views.admin_account, name='adminaccount'),
    path('employee/', views.employee, name='employee'),
    path('customer/', views.customer, name='customer'),
    path('lichdatsan/', views.lichdatsan, name='lichdatsan'),
    path('hoadon/', views.hoadon, name='hoadon'),
    path('guest/', views.guest, name='guest'),

    ]