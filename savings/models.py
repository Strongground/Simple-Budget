from datetime import date
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

User = get_user_model()
CATEGORY_ICON_CHOICES = (
    ('airplane','icon-airplane'),
    ('android','icon-android'),
    ('card','icon-card'),
    ('babymilk','icon-babymilk'),
    ('bag','icon-bag'),
    ('balloon','icon-balloon'),
    ('bandage','icon-bandage'),
    ('bikini','icon-bikini'),
    ('birthday-cake','icon-birthday-cake'),
    ('bread','icon-bread'),
    ('call','icon-call'),
    ('can-water','icon-can-water'),
    ('car','icon-car'),
    ('chair','icon-chair'),
    ('chart','icon-chart'),
    ('christmas','icon-christmas'),
    ('cocktail','icon-cocktail'),
    ('control-pad','icon-control-pad'),
    ('muffin','icon-muffin'),
    ('tool','icon-tool'),
    ('faucet','icon-faucet'),
    ('first-aid','icon-first-aid'),
    ('shoe','icon-shoe'),
    ('ice','icon-ice'),
    ('pool','icon-pool'),
    ('light-bulb','icon-light-bulb'),
    ('mask','icon-mask'),
    ('mobile','icon-mobile'),
    ('music','icon-music'),
    ('piggy-bank','icon-piggy-bank'),
    ('pizza','icon-pizza'),
    ('sewing-machine','icon-sewing-machine'),
    ('sign-board','icon-sign-board'),
    ('smartphone','icon-smartphone'),
    ('sock','icon-sock'),
    ('spoon-fork','icon-spoon-fork'),
    ('store','icon-store'),
    ('transport','icon-transport'),
    ('tooth','icon-tooth'),
    ('train','icon-train'),
    ('cart','icon-cart'),
    ('repair','icon-repair'),
    ('default','icon-simple-budget')
)

TRANSACTION_RECUR_REPEAT_DATES = (
    (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'), (6,'6'), (7,'7'), (8,'8'),
    (9,'9'), (10,'10'), (11,'11'), (12,'12'), (13,'13'), (14,'14'), (15,'15'),
    (16,'16'), (17,'17'), (18,'18'), (19,'19'), (20,'20'), (21,'21'), (22,'22'),
    (23,'23'), (24,'24'), (25,'25'), (26,'26'), (27,'27'), (28,'28')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(default='avatars/default.png', upload_to='avatars/') # This is for later implementation due to complexity
    default_account = models.ForeignKey("Account", on_delete=models.SET_NULL, blank=True, null=True)
    setting_max_transactions_days = models.IntegerField(default=10)
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Bank(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(default='static/images/bank_logos/default.png', upload_to='bank_logos/')
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
    icon_id = models.CharField(max_length=30, choices=CATEGORY_ICON_CHOICES, default='icon-simple-budget') # This references a class in a icon set
    def __str__(self):
        return self.name
    def get_icon(self):
        return 'icon-' + self.icon_id

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=100)
    is_spending = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(default=date.today)
    recurring = models.BooleanField(default=False)
    repeat_time = models.DecimalField(blank=True, null=True, decimal_places=0, max_digits=2, choices=TRANSACTION_RECUR_REPEAT_DATES)
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
