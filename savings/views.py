from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model

from .models import Account, Transaction, User, Profile
from .forms import QuickTransactionAdd

User = get_user_model()
USER_PREFERENCE_ACCOUNT_TRANSACTIONS_DAYS = 100

def index(request):
    context = {
        'account_list': Account.objects.all()
    }
    return render(request, 'savings/index.html', context)

def account(request, account_id):
    accountObj = get_object_or_404(Account, id=account_id)
    transactions = get_transactions_to_show_in_account(account_id)
    context = {
        'account': accountObj,
        'transactions': transactions
    }
    return render(request, 'savings/account.html', context)

def transaction(request, transaction_id):
    transaction_object = get_object_or_404(Transaction, id=transaction_id)
    context = {
        'transaction': transaction_object
    }
    return render(request, 'savings/transaction.html', context)

def quick_add_transaction(request):
    if request.method == 'POST':
        # Assume submitted form, validate
        form = QuickTransactionAdd(request.POST)
        if form.is_valid():
            current_transaction = Transaction()
            # Put form values in new transaction
            current_transaction.account = form.cleaned_data['account']
            current_transaction.is_spending = form.cleaned_data['is_spending']
            current_transaction.amount = form.cleaned_data['amount']
            if form.cleaned_data['description']:
                current_transaction.description = form.cleaned_data['description']
            if form.cleaned_data['category']:
                current_transaction.category = form.cleaned_data['category']
            # Save changes and redirect
            current_transaction.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully created transaction.', extra_tags='alert')
        else:
            messages.add_message(request, messages.ERROR, 'There was an error while creating the transaction.', extra_tags='alert')
        
        return HttpResponseRedirect(reverse('savings.account', kwargs={ 'account_id': current_transaction.account.id }))
        # return account(request, current_transaction.account.id, form_state)
    else:
        # Assume initial rendering
        
        # Get default user if authenticated
        if request.user.is_authenticated:
            initial_account = request.user.profile.default_account
        else:
            initial_account = None

        # Get account the user was before entering form, if any
        if 'HTTP_REFERER' in request.META:
            referer_url = request.META['HTTP_REFERER']
            if '/account/' in referer_url:
                initial_account = referer_url[(referer_url.rfind('/'))+1:]
            else:
                initial_account = None

        context = {
            'form': QuickTransactionAdd(initial={'account': initial_account}),
            'initial_account_id': initial_account,
            'initial_account_type': type(initial_account)
        }
        return render(request, 'savings/quick_add_transaction.html', context)

def get_transactions_to_show_in_account(account_id):
    end_date = date.today()
    start_date = end_date - timedelta(days=USER_PREFERENCE_ACCOUNT_TRANSACTIONS_DAYS)
    transactions = []
    for iterator in range(0,USER_PREFERENCE_ACCOUNT_TRANSACTIONS_DAYS):
        current_date = end_date - timedelta(days=iterator)
        day_transactions = Transaction.objects.filter(account__id=account_id, date=current_date)
        if day_transactions:
            transactions.append({
                'date': current_date,
                'transactions': day_transactions,
                'sum_transactions': len(day_transactions)
            })
    return transactions