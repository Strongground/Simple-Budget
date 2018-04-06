from django.urls import path, re_path
from django.conf.urls import include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Global overview of all accounts (for now)
    # 'savings'
    path('', views.index, name='index'),
    
    # Show the details and all transactions of an bank account
    # 'savings/account/1'
    path('account/<int:account_id>', views.account),

    # Show the details and all transactions of an bank account
    # 'savings/transaction/27'
    path('transaction/<int:transaction_id>', views.transaction),

    # Allow for quick adding a transaction without some details, but sufficient for fast
    # adding when on mobile. Takes no arguments.
    path('quick_add_transaction', views.quick_add_transaction),

    # Add auth urls from Django
    path('user/', include('django.contrib.auth.urls')),

    # Redirect from savings/* to /*
    # re_path(r'savings/*', RedirectView.as_view(url='/'))
]