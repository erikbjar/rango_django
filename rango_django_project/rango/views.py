from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):

    # Construct a dictionary to pass to the template engine
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client. The first parameter is the template we want to use
    return render(request, 'rango/index.html', context_dict)

def about(request):

    context_dict = {'boldmessage': "I like pizza and juice"}

    return render(request, 'rango/about.html', context_dict)
    #Use HttpResponse to add text
    #return HttpResponse("Rango says, go back to the <br/> <a href='/rango/'> index </a> page")
