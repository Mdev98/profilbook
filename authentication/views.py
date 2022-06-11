from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.

def login_page(request):
    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(email= form.cleaned_data['adresse_email'], password= form.cleaned_data['password'])
            if user is not None:
                message = "Login in success"
                login(request, user)
                return render(request, 'authentication/success.html', context={'message': message})
            else:
                message = "Identifiant incorrect"
                return render(request, 'authentication/login.html', context={'form' : form, 'message': message})
                
    
    return render(request, 'authentication/login.html', context={'form' : form})


def signup_page(request):
    form = forms.SignupForm()

    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                message = "Login in success"
                login(request, user)
                return render(request, 'authentication/success.html', context={'message': message})
            else:
                message = "Identifiant incorrect"
                return render(request, 'authentication/login.html', context={'form' : form, 'message': message})
                
    
    return render(request, 'authentication/signup.html', context={'form' : form})
