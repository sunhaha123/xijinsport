from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myindex.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def gallery(request):
    return render(request, '404.html')