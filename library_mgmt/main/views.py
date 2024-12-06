from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home_view(request):
    if user.is_superuser:  
        return redirect('admin_home')  
    else:
        return redirect('user_home')


def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:  # Check if the user is an admin
                return redirect('admin_home')  # Redirect to admin homepage
            else:
                return redirect('user_home')  # Redirect to user homepage
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')



def user_home(request):
    return render(request, 'user_home.html')


def admin_home(request):
    return render(request, 'admin_home.html')


def log_out(request):
    logout(request)
    return render(request, 'logout.html') 