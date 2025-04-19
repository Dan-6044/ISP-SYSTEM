from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [ 
      path('mikrotiks/', views.mikrotik, name='mikrotiks'),
      path('add_mikrotik/', views.add_mikrotik, name='add_mikrotik'),
      path('view_mikrotik/', views.view_mikrotik, name='view_mikrotik'),
      path('equipment/', views.equipments, name='equipment'),
      path('create-equipment/', views.create_equipments, name='create-equipment'),
      
      path('packages/', views.packages, name='packages'),
      path('create_packages/', views.create_packages, name='create_packages'),
      path('payments/', views.payments, name='payments'),
      path('add-payments/', views.add_payments, name='add_payments'),
      
      path('vouchers/', views.vouchers, name='vouchers'),
      path('add_voucher/', views.add_voucher, name='add_voucher'),
      
      path('expenses/', views.expenses, name='expenses'),
      path('add_expense/', views.add_expense, name='add_expense'),
      
      
      path('dashboard/', views.dashboard, name='dashboard'),
      path('active_users/', views.reports, name='active_users'),
      path('all_users/', views.all_users, name='all_users'),
      path('add_user/', views.add_user, name='add_user'),
      
      
      path('sms/', views.sms, name='sms'),
      path('send_sms/', views.send_sms, name='send_sms'),
      path('expiry_dates/', views.access, name='expiry_dates'),
      path('profile/', views.profile, name='profile'),

     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
