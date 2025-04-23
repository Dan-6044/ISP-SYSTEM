from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import  authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



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


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import MikroTik
from django.core.exceptions import ObjectDoesNotExist

# Add MikroTik form submission and provisioning command logic
def add_mikrotik(request):
    if request.method == 'POST':
        # Handle MikroTik name submission and proceed to provisioning
        mikrotik_name = request.POST.get('mikrotik_name')

        if not mikrotik_name:
            return render(request, 'devices/add_mikrotik.html', {'error': "MikroTik name is required."})

        # Save MikroTik name to the database or check if it already exists
        try:
            mikro, created = MikroTik.objects.get_or_create(name=mikrotik_name)
            if not created:
                return render(request, 'devices/add_mikrotik.html', {'error': "MikroTik already exists."})
        except Exception as e:
            return render(request, 'devices/add_mikrotik.html', {'error': str(e)})

        # Proceed to Step 2 (Provisioning)
        return render(request, 'devices/add_mikrotik.html', {'mikrotik_name': mikrotik_name})

    return render(request, 'devices/add_mikrotik.html')


from django.utils import timezone

def provision_device(request, mikrotik_name):
    try:
        mikrotik = MikroTik.objects.get(name=mikrotik_name)
    except ObjectDoesNotExist:
        return JsonResponse({'success': False, 'message': 'MikroTik device not found.'}, status=404)

    provisioning_url = "http://192.168.88.100/dev-provision.rsc"
    provisioning_command = f"/tool fetch url={provisioning_url} dst-path=config.rsc; /import config.rsc;"

    # Only set start time once
    if not mikrotik.provision_start_time:
        mikrotik.provision_start_time = timezone.now()
        mikrotik.save()

    return JsonResponse({
        'success': True,
        'message': 'Provisioning started. Please wait 50 seconds.',
        'command': provisioning_command
    })

from datetime import timedelta

def check_provision_status(request, mikrotik_name):
    try:
        mikrotik = MikroTik.objects.get(name=mikrotik_name)
    except ObjectDoesNotExist:
        return JsonResponse({'success': False, 'message': 'MikroTik device not found.'}, status=404)

    if not mikrotik.provision_start_time:
        return JsonResponse({'success': False, 'message': 'Provisioning has not started.'})

    elapsed = timezone.now() - mikrotik.provision_start_time

    if elapsed.total_seconds() >= 50:
        if not mikrotik.provisioned:
            mikrotik.provisioned = True
            mikrotik.save()
        return JsonResponse({'success': True, 'message': 'Provisioning completed.'})
    else:
        return JsonResponse({
            'success': False,
            'message': f'Provisioning in progress. Please wait {int(50 - elapsed.total_seconds())} seconds.'
        })









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