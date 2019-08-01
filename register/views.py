from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache

from register.forms import RegisterForm, UpdateProfileForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('dashboard.home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile_view(request):
    # if request.method == 'POST':
    #     form = EditProfileForm(request.POST or None)
    #     if form.is_valid():
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         location = form.cleaned_data['location']
    #         bio = form.cleaned_data['bio']
    #         print(form)
    form = UpdateProfileForm(request.POST or None)
    print(form)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'test-form.html', context)


@never_cache
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        raw_password = request.POST.get('password', '')
        user = authenticate(username=username, password=raw_password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard.home')
        else:
            return redirect('login')
    else:
        if not request.user.is_authenticated:
            return render(request, 'login.html')


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
