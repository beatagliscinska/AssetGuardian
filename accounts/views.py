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
    try:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            if request.method == 'POST':
                form = CustomCreateUserForm(request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    try:
                        # Attempt to save the user
                        form.save()
                        user = form.cleaned_data.get('username')
                        messages.success(request, 'Account was created for ' + user)
                        return redirect('user_login')
                    except IntegrityError:
                        # Handle the case where the username already exists
                        messages.error(request, 'Username is already taken.')
            else:
                form = CustomCreateUserForm()

            context = {'form': form}
            return render(request, 'accounts/register.html', context)

    except Exception as e:
        # Log the exception or handle it appropriately
        messages.error(request, 'An error occurred during registration.')
        # You might want to log the exception for debugging purposes
        # logging.error(str(e))
        return redirect('home')  # Redirect to a generic error page or home page


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




# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user = request.user
#         form = CustomChangeUserForm(request.POST, request.FILES, instance=user)
#         if form.is_valid():
#             user_form = form.save()
#
#             messages.success(request, 'Your profile has been updated!')
#             return redirect('profile', user_form.username)
#
#         for error in list(form.errors.values()):
#             messages.error(request, error)
#
#     user = get_user_model().objects.filter(username=request.user.username).first()
#     if user:
#         form = CustomChangeUserForm(instance=user)
#         return render(request, 'accounts/profile.html', context={'form': form})
#
#     return redirect("home")
