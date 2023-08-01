from django.shortcuts import render
from .forms import SignUpForm

def custom_login_view(request):
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
