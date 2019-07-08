from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/")
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def mailbox(request):
    return render(request, 'mailbox.html')
