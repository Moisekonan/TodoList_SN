from django.urls import path

from tasks.views import index, create_task, update_task, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_task, name='create_task'),
    path('update/<int:pk>/', update_task, name='update_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task')
]
