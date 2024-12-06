from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import MembershipForm, UpdateMembershipForm, MediaForm, UpdateMediaForm, UserProfileForm


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


def log_out(request):
    logout(request)
    return render(request, 'logout.html') 


from django.shortcuts import render, redirect
from .forms import MembershipForm, UpdateMembershipForm, MediaForm, UpdateMediaForm, UserProfileForm


def admin_home(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        # Handle Membership Add/Update
        if action == 'add_membership':
            form = MembershipForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_home')
        elif action == 'update_membership':
            form = UpdateMembershipForm(request.POST)
            if form.is_valid():
                # Logic to update membership (implement as needed)
                pass

        # Handle Media Add/Update
        elif action == 'add_media':
            form = MediaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_home')
        elif action == 'update_media':
            form = UpdateMediaForm(request.POST)
            if form.is_valid():
                # Logic to update media (implement as needed)
                pass

        # Handle User Management Add/Update
        elif action == 'add_update_user':
            form = UserProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_home')

    return render(request, 'admin_home.html', {
        'membership_form': MembershipForm(),
        'update_membership_form': UpdateMembershipForm(),
        'media_form': MediaForm(),
        'update_media_form': UpdateMediaForm(),
        'user_profile_form': UserProfileForm(),
    })
