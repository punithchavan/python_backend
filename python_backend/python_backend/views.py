from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world, Python backend Django Home page")
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')
