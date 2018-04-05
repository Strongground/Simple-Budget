from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    # Global overview of all accounts (for now)
    # 'savings'
    path('', views.index, name='index'),
    
    # Show the details and all transactions of an bank account
    # 'savings/account/1'
    path('account/<int:account_id>', views.account),

    # Show the details and all transactions of an bank account
    # 'savings/account/1'
    path('transaction/<int:transaction_id>', views.transaction),

    # Allow for quick adding a transaction without some details, but sufficient for fast
    # adding when on mobile. Takes no arguments.
    path('quick_add_transaction', views.quick_add_transaction),

    # Add auth urls from Django
    path('user/', include('django.contrib.auth.urls')),

    # Login/Logout pages
    path('login/', views.login),
    path('login/', views.logout)
]