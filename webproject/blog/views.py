from django.shortcuts import render, get_object_or_404, redirect
from .models import Categories, Post

# Create your views here.

def blog(request):
    categories = Categories.objects.all()
    return render(request, 'blog/blog.html', {'categories':categories})

def topics_view(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'blog/topics_view.html', {'category':category})

