from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company.list'),
    path('companies/create/', views.CompanyCreate.as_view(), name='company.create'),
    path('companies/update/<int:pk>/', views.CompanyUpdate.as_view(), name='company.update'),
    path('companies/delete/<int:pk>/', views.CompanyDelete.as_view(), name='company.delete'),

    path('projects/', views.ProjectList.as_view(), name='project.list'),
    path('projects/create/', views.ProjectCreate.as_view(), name='project.create')
]
