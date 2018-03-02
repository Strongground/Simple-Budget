from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Account, Transaction, User, Profile
from .forms import QuickTransactionAdd

def index(request):
    context = {
        'account_list': Account.objects.all()
    }
    return render(request, 'savings/index.html', context)

def account(request, account_id):
    accountObj = get_object_or_404(Account, id=account_id)
    context = {
        'account': accountObj,
        'transactions': Transaction.objects.filter(account__id=account_id)
    }
    return render(request, 'savings/account.html', context)

def transaction(request, transaction_id):
    transaction_object = get_object_or_404(Transaction, id=transaction_id)
    context = {
        'transaction': transaction_object
    }
    return render(request, 'savings/transaction.html', context)

def quick_add_transaction(request):
    current_user = User.objects.get(username='noel')
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
        transaction_object = get_object_or_404(Transaction, id=transaction.id)
        context = {
            'return_state': form_state,
            'transaction': transaction_object
        }
        return render(request, 'savings/transaction.html', context)
    else:
        # Assume initial rendering
        context = {
            'form': QuickTransactionAdd(initial={'account': current_user.profile.default_account})
        }
        return render(request, 'savings/quick_add_transaction.html', context)

def create_message(state, title, body):
    message = {
        'state': state,
        'title': title,
        'body': body
    }
    return message