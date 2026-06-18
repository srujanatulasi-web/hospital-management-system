from django.urls import path
from .views import appointments_list, appointments_edit, appointments_create, appointments_delete
urlpatterns = [
    path('',appointments_list),
    path('<int:pk>/edit/', appointments_edit),
    path('create/', appointments_create),
    path('<int:pk>/delete/', appointments_delete),
    
]