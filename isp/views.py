from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



#### LANDING PAGE ##

def home(request):
    
    return render(request, 'Pages/landingPage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the new user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user_id = user.id  # Get the user's ID

            # Log the user in automatically after registration
            login(request, user)
            return redirect('mikrotiks')  # Redirect to home after successful registration
        else:
            # Pass the form errors to the template
            return render(request, 'signing.html', {'form': form, 'signup_errors': form.errors})

    else:
        form = SignupForm()

    return render(request, 'signing.html', {'form': form})

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Ensure email and password are provided
        if not email or not password:
            messages.error(request, "Both email and password are required.", extra_tags="login_error")
            return redirect('signin')

        # Get user by email
        user = User.objects.filter(email=email).first()

        if user:
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user:
                auth_login(request, authenticated_user)
                return redirect(reverse('mikrotiks'))  # Redirect to dashboard
            else:
                messages.error(request, "Invalid email or password.", extra_tags="login_error")
        else:
            messages.error(request, "Invalid email or password.", extra_tags="login_error")

    return render(request, 'signing.html')  # Ensure the correct template name




def mikrotik(request):
    
    return render(request, 'devices/mikrotik.html')


# views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MikroTik
from time import sleep

def add_mikrotik(request):
    step = request.GET.get('step', '1')  # Default to step 1

    if request.method == 'POST':
        if step == '1':  # Step 1: Save MikroTik name
            mikrotik_name = request.POST.get('mikrotik_name')
            mikrotik = MikroTik.objects.create(name=mikrotik_name)
            return redirect('add_mikrotik', step='2', mikrotik_id=mikrotik.id)

        elif step == '2':  # Step 2: Generate command and provisioning status
            mikrotik_id = request.POST.get('mikrotik_id')
            mikrotik = MikroTik.objects.get(id=mikrotik_id)
            provision_command = f"/interface ethernet set ether1 name={mikrotik.name}_ether1"
            mikrotik.provisioning_command = provision_command
            mikrotik.save()

            # Simulate provisioning process
            attempt_count = 0
            while attempt_count < 20:
                sleep(2)
                attempt_count += 1
                mikrotik.provisioning_status = f'Attempt {attempt_count}/20'
                mikrotik.save()
                if attempt_count == 20:
                    mikrotik.provisioning_status = 'Provisioning Failed'
                    mikrotik.save()
                    break
                else:
                    mikrotik.provisioning_status = f'Attempt {attempt_count}/20'
                    mikrotik.save()

            return redirect('add_mikrotik', step='3', mikrotik_id=mikrotik.id)

        elif step == '3':  # Step 3: Configure MikroTik (PPPoE or Hotspot)
            mikrotik_id = request.POST.get('mikrotik_id')
            mikrotik = MikroTik.objects.get(id=mikrotik_id)
            mikrotik.is_ppoe = request.POST.get('is_ppoe') == 'on'
            mikrotik.save()
            return redirect('mikrotik_list')  # Redirect to a list page or confirmation

    mikrotik = MikroTik.objects.filter(id=request.GET.get('mikrotik_id')).first() if step != '1' else None
    return render(request, 'devices/add_mikrotik.html', {'step': step, 'mikrotik': mikrotik})






def view_mikrotik(request):
    
    return render(request, 'devices/view_mikrotiks.html')

def equipments(request):
    
    return render(request, 'devices/equipments.html')

def create_equipments(request):
    
    return render(request, 'devices/create-equipments.html')

def dashboard(request):
    
    return render(request, 'dashboard/dashboard.html')

def reports(request):
    
    return render(request, 'dashboard/reports.html')


def vouchers(request):
    
    return render(request, 'finances/vouchers.html')

def add_voucher(request):
    
    return render(request, 'finances/add_voucher.html')

def add_voucher(request):
    
    return render(request, 'finances/add_voucher.html')


def view_clients(request):
    
    return render(request, 'clients/view_clients.html')


def packages(request):
    
    return render(request, 'finances/packages.html')

def create_packages(request):
    
    return render(request, 'finances/create_packages.html')

def payments(request):
    
    return render(request, 'finances/payments.html')

def add_payments(request):
    
    return render(request, 'finances/add_payments.html')

def view_plans(request):
    
    return render(request, 'finances/view_plans.html')

def all_users(request):
    
    return render(request, 'users/users.html')

def add_user(request):
    
    return render(request, 'users/add_user.html')

def billings(request):
    
    return render(request, 'finances/vouchers.html')


def expenses(request):
    
    return render(request, 'finances/expenses.html')

def add_expense(request):
    
    return render(request, 'finances/add_expenses.html')

def access(request):
    
    return render(request, 'user/access.html')

def profile(request):
    
    return render(request, 'user/profile.html')

def sms(request):
    
    return render(request, 'communications/sms.html')

def send_sms(request):
    
    return render(request, 'communications/send-sms.html')