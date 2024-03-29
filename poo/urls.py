from django.contrib import admin
from django.urls import path, include
from acolhe.views import geral, acolhido, anfitriao
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('acolhe.urls')),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
