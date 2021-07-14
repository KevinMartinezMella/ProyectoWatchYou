from django.urls import path
from . import views

app_name='licencias'


urlpatterns=[
    path('',views.index, name='index'),
]