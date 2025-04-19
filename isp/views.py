from django.shortcuts import render


def mikrotik(request):
    
    return render(request, 'devices/mikrotik.html')

def add_mikrotik(request):
    
    return render(request, 'devices/add_mikrotik.html')

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