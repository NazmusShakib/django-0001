from django.shortcuts import render


def register(request):
    print(request.POST)
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
