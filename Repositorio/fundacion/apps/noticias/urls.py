from django.urls import path

from . import views

app_name = 'noticias'

urlpatterns = [
    
    path('listar/', views.Listar, name = 'listar_noticias'),

    path('detalle/<int:pk>', views.Detalle_Noticia, name = 'detalle_noticias'),

    ]

