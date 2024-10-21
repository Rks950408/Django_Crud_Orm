# crud_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_emp/', views.create, name='create'), 
    path('retrieve_emp/', views.reterive, name='retrieve'),  
    path('delete_emp/<int:emp_id>/', views.delete_emp, name='delete_emp'), 
    path('update/<int:emp_id>/', views.update_emp, name='update'), 

]
