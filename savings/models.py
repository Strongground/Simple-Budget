from datetime import date
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(default='avatars/default.png', upload_to='avatars/') # This is for later implementation due to complexity
    default_account = models.ForeignKey("Account", on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Bank(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default='static/images/bank_logos/default.png', upload_to='static/images/bank_logos/')
    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    balance = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    bank = models.ForeignKey(Bank, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name
    def update(self, single_transaction=None, reverse=False):
        if single_transaction:
            if single_transaction.is_spending:
                if reverse:
                    self.balance += single_transaction.amount
                else:
                    self.balance -= single_transaction.amount
            else:
                if reverse:
                    self.balance -= single_transaction.amount
                else:
                    self.balance += single_transaction.amount
        else:
            transactions = Transaction.objects.get(account__self)
            new_balance = 0
            for transaction_to_process in transactions:
                if transaction_to_process.is_spending:
                    new_balance -= transaction_to_process.amount
                else:
                    new_balance += transaction_to_process.amount
            self.balance = new_balance
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=1) # This references a character in a icon set
    def __str__(self):
        return self.name

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=100)
    is_spending = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(default=date.today)
    recurring = models.BooleanField(default=False)
    repeat_time = models.DurationField(blank=True, null=True)
    def __str__(self):
        return self.description + ': ' + str(self.amount) + '€'

# Receivers
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=Transaction)
def update_account(sender, instance, created, **kwargs):
    if created:
        instance.account.update(instance)

@receiver(post_delete, sender=Transaction)
def update_account_on_deletion(sender, instance, **kwargs): 
    instance.account.update(instance, reverse=True)
