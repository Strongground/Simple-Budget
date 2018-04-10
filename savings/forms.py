from django import forms
from .models import Category, Account, Transaction

class QuickTransactionAdd(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all())
    description = forms.CharField(help_text="Description of the transaction", required=False)
    is_spending = forms.BooleanField(initial=True, required=False)
    amount = forms.DecimalField(max_digits=100, decimal_places=2)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=False, required=False)

    def is_valid(self):
        # run the parent validation first
        valid = super(QuickTransactionAdd, self).is_valid()
        if not valid:
            return valid

        # run additional validations
        amount = self.cleaned_data['amount']
        if not amount > 0:
            return False
        
        return True