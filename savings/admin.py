from django.contrib import admin
from .models import Profile, Bank, Account, Category, Transaction

# Register your models here.
admin_models = [Profile, Bank, Account, Category, Transaction]
admin.site.register(admin_models)
