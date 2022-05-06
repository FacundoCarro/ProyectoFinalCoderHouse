from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Felicitaciones, se ha registrado satisfactoriamente")
            return redirect('Inicio')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('Inicio')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            # We check if the data is correct
            user = authenticate(email=email, password=password)
            if user:  # If the returned object is not None
                auth_login(request, user)  # we connect the user
                return redirect('Inicio')
            else:  # otherwise an error will be displayed
                messages.error(request, 'Correo o contraseña erronea')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect(reverse('accounts:login'))
