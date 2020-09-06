from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'App/home.html')

def shop(request):
    return render(request, 'App/shop.html')

def contact(request):
    return render(request, 'App/contact.html')

def blog(request):
    return render(request, 'App/blog.html')
