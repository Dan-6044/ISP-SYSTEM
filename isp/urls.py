from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [ 
      path('mikrotiks/', views.add_mikrotik, name='mikrotiks'),
      path('view_mikrotik/', views.view_mikrotik, name='view_mikrotik'),
      path('equipment/', views.equipments, name='equipment'),
      path('create-equipment/', views.create_equipments, name='create-equipment'),
      
      path('packages/', views.packages, name='packages'),
      path('create_packages/', views.create_packages, name='create_packages'),
      path('payments/', views.payments, name='payments'),
      path('add-payments/', views.add_payments, name='add_payments'),
      
      path('vouchers/', views.add_clients, name='vouchers'),
      path('expenses/', views.view_clients, name='expenses'),
      
      
      path('dashboard/', views.dashboard, name='dashboard'),
      path('active_users/', views.reports, name='active_users'),
      path('all_users/', views.transactions, name='all_users'),
      
      
      path('sms/', views.sms, name='sms'),
      path('send_sms/', views.send_sms, name='send_sms'),
      path('campaigns/', views.access, name='campaigns'),
      path('profile/', views.profile, name='profile'),

     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
