from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard.home"),
    path("mailbox/", views.mailbox, name="dashboard.mailbox"),
]