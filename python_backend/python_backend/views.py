from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world, Python backend Django Home page")

def about(request):
    return HttpResponse("Im Punith, Django developer")

def contact(request):
    return HttpResponse("You can connect me on linkedIn")
