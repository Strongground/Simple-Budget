from datetime import date
from django import forms
from .models import Category, Account, Transaction

TRANSACTION_RECUR_REPEAT_DATES = (
    (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'), (6,'6'), (7,'7'), (8,'8'),
    (9,'9'), (10,'10'), (11,'11'), (12,'12'), (13,'13'), (14,'14'), (15,'15'),
    (16,'16'), (17,'17'), (18,'18'), (19,'19'), (20,'20'), (21,'21'), (22,'22'),
    (23,'23'), (24,'24'), (25,'25'), (26,'26'), (27,'27'), (28,'28')
)

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

class AddTransaction(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all())
    description = forms.CharField(help_text="Description of the transaction.", required=False)
    is_spending = forms.BooleanField(initial=True, required=False, help_text="Is this a spending or a earning?")
    amount = forms.DecimalField(max_digits=100, decimal_places=2)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=False, required=False)
    date = forms.DateField(initial=date.today, help_text="When this transaction occured.")
    recurring = forms.BooleanField(initial=False, required=False, label="Recurring Transaction", help_text="Is this a transaction that is repeated on a regular basis?")
    repeat_time = forms.ChoiceField(choices=TRANSACTION_RECUR_REPEAT_DATES, help_text="Only required if 'recurring' is selected.")

    def is_valid(self):
        # run the parent validation first
        valid = super(AddTransaction, self).is_valid()
        if not valid:
            return valid
        # run additional validations
        amount = self.cleaned_data['amount']
        if not amount > 0:
            return False
        return True
    
    def clean(self):
        # make sure required dependent fields are handled correct
        recurring = self.cleaned_data.get('recurring')
        if recurring:
            self.fields_required(['repeat_time'])
        else:
            self.cleaned_data['repeat_time'] = ''
        return self.cleaned_data
    
    def fields_required(self, fields):
        """Used for conditionally marking fields as required."""
        for field in fields:
            if not self.cleaned_data.get(field, ''):
                msg = forms.ValidationError("This field is required.")
                self.add_error(field, msg)

class UpdateTransaction(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'description', 'is_spending', 'amount', 'category', 'date', 'recurring', 'repeat_time']

class DeleteTransaction(forms.Form):
    # delete = forms.BooleanField(initial=False, required=False, widget=forms.HiddenInput)
    pass