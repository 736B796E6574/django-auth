
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to a specific page after successful login (You can change 'home' to the desired URL name)
            return redirect('loggedin')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')
    

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loggedin_view(request):
    return render(request, 'loggedin.html')

def logout_view(request):
    logout(request)
    return redirect('loggedout')  # Replace 'home' with the URL name or path to redirect after logout

def loggedout_view(request):
    return render(request, 'loggedout.html')