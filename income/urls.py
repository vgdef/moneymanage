from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('income/', views.income, name='income'),
    path('income/details/<int:id>', views.details, name='details'),
]