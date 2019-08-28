from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def companyList(request):
    return render(request, 'company-list.html')


@login_required
def companyCreate(request):
    return render(request, 'company-form.html')
