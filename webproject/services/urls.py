from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^servicios/$', views.services_view, name='services'),
    re_path(r'^servicios/(?P<pk>\d+)/$', views.service_view, name='service'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)