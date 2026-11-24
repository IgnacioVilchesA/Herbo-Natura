from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('catalogo/', views.catalogo, name='catalogo'),

    path('nosotros/', views.nosotros, name='nosotros'),

    path('contacto/', views.contacto, name='contacto'),
]