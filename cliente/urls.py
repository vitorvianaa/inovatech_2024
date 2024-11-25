from .views import form, pontos_coleta, home, servicos, about
from django.urls import path


urlpatterns = [
    path('form/', form, name='form'),
    path('index/services/', servicos, name = 'servicos'),
    path('index/about/', about, name='sobre'),
    path('index/', home, name='home'), 
    path('pontos-coleta/', pontos_coleta, name='pontos_coleta'),
]