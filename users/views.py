from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomUserLoginForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_picture = 'path/to/default_profile_picture.jpg'
            user.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Your account for {email} has been created! You can login now!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.email}!')
                return redirect('profile')
            else:
                return render(request, 'users/login.html', {'form': CustomUserLoginForm(),'user': "wrong"})  
    else:
        form = CustomUserLoginForm()

    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

''' Valid messages
        messages.debug
        messages.info
        messages.success
        messages.error
        messages.warning
        Similar to ruby flash messages
'''