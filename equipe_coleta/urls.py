from django.urls import path
from .views import exibir_tasks, detalhe_task, mudar_status

urlpatterns = [
    path('tasks/', exibir_tasks, name='exibir_tasks'),
    path('tasks/<int:id>', detalhe_task, name='detalhe_task'),
    path('tasks/<int:id>/mudar-status', mudar_status, name='mudar_status')
]