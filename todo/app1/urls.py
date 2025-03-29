from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:id>',edit,name="edit"),  # Fix edit path
    # path('delete/<int:id>/', views.delete_task, name="delete"),  # Fix delete path
]