from django.shortcuts import render
from .models import Categories

# Create your views here.

def blog(request):
    categories = Categories.objects.all()
    return render(request, 'blog/blog.html', {'categories':categories})
