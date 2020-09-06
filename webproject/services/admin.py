from django.contrib import admin
from .models import Services

# Register your models here.

class Services_admin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')

admin.site.register(Services, Services_admin)
