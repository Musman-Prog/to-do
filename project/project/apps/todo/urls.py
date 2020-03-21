from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('complete/<todo_id>', views.complete, name='complete'),
    path('notcomplete/<todo_id>', views.notcomplete, name='notcomplete'),
    path('delete/<todo_id>', views.delete, name='delete'),
    path('deleteall', views.delete_all, name='delete_all'),
]