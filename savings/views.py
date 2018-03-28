from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import date, timedelta
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
    # @TODO Add some kind of protection against accidental reloading which creates another identical transaction
    if request.method == 'POST':
        # Assume submitted form, validate
        form = QuickTransactionAdd(request.POST)
        if form.is_valid():
            transaction = Transaction()
            # Put form values in new transaction
            transaction.account = form.cleaned_data['account']
            transaction.is_spending = form.cleaned_data['is_spending']
            transaction.amount = form.cleaned_data['amount']
            if form.cleaned_data['description']:
                transaction.description = form.cleaned_data['description']
            if form.cleaned_data['category']:
                transaction.category = form.cleaned_data['category']
            # Save changes and redirect
            transaction.save()
            form_state = create_message('success', 'Success!', 'Successfully created transaction.')
        else:
            form_state = create_message('error', 'Error!', 'There was an error while creating the transaction.')
        
        context = {
            'return_state': form_state,
            'account_object': transaction.account
        }
        return render(request, 'savings/account.html', context)
    else:
        # Assume initial rendering
        if request.user.is_authenticated:
            user_default_account = request.user.profile.default_account
        else:
            user_default_account = None

        context = {
            'form': QuickTransactionAdd(initial={'account': user_default_account})
        }
        return render(request, 'savings/quick_add_transaction.html', context)

def create_message(state, title, body):
    message = {
        'state': state,
        'title': title,
        'body': body
    }
    return message