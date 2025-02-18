from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def adminsystem(request):
    return HttpResponse(request, 'hello world')

def admin_account(request):
    return HttpResponse(request, 'hello world')

def employee(request):
    return HttpResponse(request, 'hello world')

def customer(request):
    return HttpResponse(request, 'hello world')

def lichdatsan(request):
    return HttpResponse(request, 'hello world')

def hoadon(request):
    return HttpResponse(request, 'hello world')

def guest(request):
    return HttpResponse(request, 'hello world')