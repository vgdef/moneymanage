from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('income/', views.income, name='income'),
    path('income/details/<int:id>', views.details, name='details'),
    path('income/income_entry/', views.income_entry, name='income_entry'),
    path('income/delete/<int:id>', views.delete, name='delete'),
    path('income/update/<int:id>', views.update, name='update'),
    path('income/update/update_record/<int:id>', views.update_record, name='update_record'),
    path('reference/', views.reference, name='reference'),
    path('need/', views.need, name='need'),

]