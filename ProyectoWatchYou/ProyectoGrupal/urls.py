from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.master.urls')),
    path('usuarios',include('apps.usuarios.urls')),
    path('servidores',include('apps.servidores.urls'))
]
