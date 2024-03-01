from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.forms import CustomCreateUserForm, CustomChangeUserForm
from accounts.models import CustomUser

from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError


def register_page(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in.')
        return redirect('home')

    if request.method == 'POST':
        form = CustomCreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}. You can now login.')
            return redirect('user_login')
    else:
        form = CustomCreateUserForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect.')
        context = {}
        return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return render(request, 'accounts/logout.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

