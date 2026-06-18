from django.urls import path
from .views import doctor_list, doctor_edit, doctor_create, doctor_delete

urlpatterns = [
    path('',doctor_list),
    path('<int:pk>/edit/', doctor_edit),
    path('create/', doctor_create),
    path('<int:pk>/delete/', doctor_delete),
    
]