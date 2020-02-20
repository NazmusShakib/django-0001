from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache

from register.forms import RegisterForm, UpdateProfileForm, UserUpdateForm


def register(request):
    if request.method == 'POST':
        print(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            username = form.cleaned_data.get('email')
            print(username)
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('dashboard.home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
@transaction.atomic
def profile_view(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST or None, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if user_update_form.is_valid() and profile_form.is_valid():
            user_update_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
        else:
            print(user_update_form.errors)
            print(profile_form.errors)
            messages.error(request, 'Please correct the error below.')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_update_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context)


@never_cache
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        raw_password = request.POST.get('password', '')
        user = authenticate(username=username, password=raw_password)

        if user is not None:
            auth_login(request, user)
    else:
        if not request.user.is_authenticated:
            return render(request, 'login.html')

    return redirect('dashboard.home')


def logout_view(request):
    logout(request)
    return redirect('login')


def handler404(request, exception):
    """
     Page not found Error 404
    """
    return render(request, 'errors/404.html', status=404)


def handler500(request, exception):
    """
     Server Error 500
    """
    return render(request, 'errors/500.html', status=500)
