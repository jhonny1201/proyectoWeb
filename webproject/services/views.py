from django.shortcuts import render, get_object_or_404, redirect
from .models import Services

# Create your views here.

def services_view(request):
    services = Services.objects.all()
    return render(request, 'services/services_view.html', {'services':services})

def service_view(request, pk):
    service = get_object_or_404(Services, pk=pk)
    return render(request, 'services/service_view.html', {'service':service})