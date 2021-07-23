from django.urls import path
from . import views

app_name='master'


urlpatterns=[
    path('',views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('devices', views.devices, name='devices'),
    path('cerrar',views.cerrar,name='cerrar'),
    path('nuevo_srv',views.nuevo_srv,name='nuevo_srv'),
    path('delete/<int:idserver>',views.erase,name='delete'),
    path('edit/<int:idserver>',views.edit,name='edit'),
    path('programar',views.programar,name='programar'),
    path('probar',views.multiThread,name='probar'),
    path('menu',views.menu, name='menu')
    # path('datos', views.datos, name='datos'),
]