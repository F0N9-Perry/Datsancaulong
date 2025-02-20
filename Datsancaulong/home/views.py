from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from adminsystem.models import LichDatSan

# Create your views here.


def home(request):
    return render(request, "home.html")

def lichdatsan(request):
    lichdatsan = LichDatSan.objects.all()
    template = loader.get_template('home/LichDatSan.html')
    context = {
        'lichdatsan': lichdatsan,
    }
    return HttpResponse(template.render(context, request))

def edit_lichdatsan(request):
    lichdatsan = LichDatSan.objects.get( id = 1)
    template= loader.get_template('home/LichDatSan-edit.html')
    context = {
        'lichdatsan': lichdatsan,
    }
    return HttpResponse(template.render(context, request))