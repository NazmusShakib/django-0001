from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('companies/', views.CompanyList.as_view(), name='company.list'),
    path('companies/create/', views.CompanyCreate.as_view(), name='company.create')
]
