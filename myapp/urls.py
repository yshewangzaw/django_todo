from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]


