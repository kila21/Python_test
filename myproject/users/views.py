from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def login_user(request):
    if request == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'])
            login(request, user)
            return HttpResponse('You are Logged In')
    form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    return HttpResponse('USER LOGOUT')
    