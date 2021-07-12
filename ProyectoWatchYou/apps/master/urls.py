from django.urls import path
from . import views

app_name='master'


urlpatterns=[
    path('',views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('devices', views.devices, name='devices'),
    path('cerrar',views.cerrar,name='cerrar'),
    path('nuevo_srv',views.nuevo_srv,name='nuevo_srv')
]