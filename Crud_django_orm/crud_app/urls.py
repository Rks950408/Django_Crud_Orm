# crud_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_emp/', views.create, name='create'),  # Create view
]
