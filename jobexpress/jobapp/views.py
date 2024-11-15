from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Job
from .forms import JobForm, UserRegistrationForm, AdminRegistrationForm

# Home Page
def home(request):
    return render(request, 'home.html')

# Admin Dashboard
@login_required
def admin_dashboard(request):
    if request.user.is_superuser:
        jobs = Job.objects.all()
        if request.method == "POST" and 'logout' in request.POST:
            logout(request)  
            return redirect('home')  
        return render(request, 'admin_dashboard.html', {'jobs': jobs})
    return redirect('home')

# Post Job (Admin only)
@login_required
def post_job(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = JobForm(request.POST)
            if form.is_valid():
                job = form.save(commit=False)
                job.posted_by = request.user
                job.save()
                return redirect('admin_dashboard')
        else:
            form = JobForm()
        return render(request, 'post_job.html', {'form': form})
    return redirect('home')

# User Dashboard
@login_required
def user_dashboard(request):
    if not request.user.is_superuser:
        jobs = Job.objects.all()
        if request.method == "POST" and 'logout' in request.POST:
            logout(request)  
            return redirect('home')  
        return render(request, 'user_dashboard.html', {'jobs': jobs})
    return redirect('home')

# Admin Login
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:  
            login(request, user)
            return redirect('admin_dashboard')  
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid admin credentials'})
    
    return render(request, 'admin_login.html')

# User Login
def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('admin_dashboard')
        return redirect('user_dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('admin_dashboard')
                return redirect('user_dashboard')
            else:
                form.add_error(None, "Invalid username or password")
        else:
            form.add_error(None, "Please correct the errors below.")
    else:
        form = AuthenticationForm()

    return render(request, 'user_login.html', {'form': form})

# User Registration
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Your account has been created!')
            return redirect('login') 
    else:
        form = UserCreationForm()

    return render(request, 'user_register.html', {'form': form})



# Admin Registration
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('admin_dashboard')  
    else:
        form = AdminRegistrationForm()
    return render(request, 'admin_register.html', {'form': form})

# All Users (Admin only)
@login_required
def all_users(request):
    if request.user.is_superuser:
        users = User.objects.all()  
        return render(request, 'all_users.html', {'users': users})
    return redirect('home')

# About and Contact Page
def about_contact(request):
    return render(request, 'about_contact.html')

# Logout
def logout_view(request):
    logout(request)  
    return redirect('login')  
def delete_job(request, job_id):
    if request.method == 'POST':
        try:
            job = Job.objects.get(id=job_id)
            job.delete()
        except Job.DoesNotExist:
            pass  
    
    return redirect('admin_dashboard')
