"""Users Views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exceptions
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

def login_view(req):
    """Login View."""
    if req.method == 'POST':

        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)

        if user:
            login(req, user)
            return redirect('feed') # <-- Le ponesmos el sobrenombre al path del feed y sabe a donde ir
        else:
            return render(req, 
            'users/login.html', 
            {'error': 'Invalid username or password'})

    return render(req, 'users/login.html')


@login_required
def logout_view(req):
    """Logout a user."""
    logout(req)
    return redirect('login')


def signup(req):
    """Signup view."""
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        password_confirmation = req.POST['password_confirmation']

        # Si las contraseñas no coinciden mandamos a la pagina la validación
        if password != password_confirmation:
            return render(req, 'users/signup.html', {'error': 'Passwords doesn\'t match!'})

        # Registramos el usuario invocando al modelo y en un try por si ingresan el usuario repetido
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(req, 'users/signup.html', {'error': 'Username already in use!'})
        
        user.first_name = req.POST['first_name']
        user.last_name = req.POST['last_name']
        user.email = req.POST['email']
        user.save() # Guardamos siempre lo que recibimos de POST

        profile = Profile(user=user)
        profile.save() # Guardamos siempre lo que recibimos de POST

        return redirect('login')

    return render(req, 'users/signup.html')


def update_profile(req):
    """Update user's Profile view."""
    return render(req, 'users/update_profile.html')