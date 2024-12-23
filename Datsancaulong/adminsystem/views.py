from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def adminsystem (request):
    return render(request, 'adminsystem/adminsystem.html')