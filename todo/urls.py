from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('', views.list, name='home'),
    path('delete/<int:id>', views.delete, name = 'delete')
]
