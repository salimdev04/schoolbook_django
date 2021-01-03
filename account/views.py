from django import forms
from django.http.response import HttpResponse
from account.forms import LoginForm, UserRegistrationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from .models import Profile
# Create your views here.


def user_login(request):
    if request.method == 'GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {
        'form': form
    })


def register(request):
    if request.method == 'GET':
        user_form = UserRegistrationForm(request.GET)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('index')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {
        'user_form': user_form
    })


def edit(request):
    if request.method == 'POST':
        user_form = User
