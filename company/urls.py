from django.urls import path

from . import views

urlpatterns = [
    path('companies/', views.companyList, name='company.list'),
    path('companies/create/', views.companyCreate, name='company.create')
]
