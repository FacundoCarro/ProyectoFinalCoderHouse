from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Inicio')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})