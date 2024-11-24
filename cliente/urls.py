from .views import form, pontos_coleta
from django.urls import path


urlpatterns = [
    path('form/', form, name='form'),
    path('pontos-coleta/', pontos_coleta, name='pontos_coleta'),
]