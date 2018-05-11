from django.urls import path, re_path
from django.conf.urls import include, url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Global overview of all accounts
    # e.g. '/'
    path('', views.index, name='index'),
    
    # Show the details and all transactions of an bank account
    # e.g. '/account/1'
    path('account/<int:account_id>', views.account, name='account'),

    # Show the details of a transaction and allow to change values of it
    # e.g. '/transaction/27'
    path('update_transaction/<int:transaction_id>', views.update_transaction, name='update_transaction'),

    # Allow for quick adding a transaction without some details, but sufficient for fast
    # adding when on mobile. Takes no arguments.
    path('quick_add_transaction/', views.quick_add_transaction, name='quick_add_transaction'),

    # Allow creation of a new transaction with all features of the model
    path('add_transaction/', views.add_transaction, name='add_transaction'),

    # Add auth urls from Django
    path('user/', include('django.contrib.auth.urls')),

    # Show, add and delete categories
    path('categories/', views.categories, name='categories'),

    # Modify category or create new
    # e.g. '/update_category/7'
    path('update_category/<int:category_id>', views.update_category, name='update_category'),
]
