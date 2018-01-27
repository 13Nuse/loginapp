from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from useraccount.forms import RegistrationForm, EditProfileForm


@login_required
def index(request):
    numbers = [8572774282]
    name = "Savan Yim"
    args = {"myname": name, "numbers": numbers}
    return render(request, 'useraccount/home.html', args)


def base(request):
    return render(request, 'base/header.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/useraccount/home')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'useraccount/reg_form.html', args)


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'useraccount/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/useraccount/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'useraccount/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/useraccount/profile')
        else:
            return redirect('/useraccount/change_password.html')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'useraccount/change_password.html', args)
