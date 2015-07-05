from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world!, here is the <br/> <a href='/rango/about' about </a> page")

def about(request):
    return HttpResponse("Rango says, go back to the <br/> <a href='/rango/'> index </a> page")
