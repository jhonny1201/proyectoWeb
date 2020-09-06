from django.shortcuts import render
from .models import Services

# Create your views here.

def service_view(request):
    services = Services.objects.all()
    return render(request, 'services/service_view.html', {'services':services})