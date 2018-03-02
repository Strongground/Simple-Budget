# Simple Budget App
Add transactions to accounts, categorize and visualize spendings and earnings, with multiple users/accounts possible.

## Easy development start
Get interactive shell for API test running:
```python
$> python3 manage.py shell
>>> from savings.models import Transaction, Profile, Account, Bank, Category
```

Start server with auto-polling:
```python
$> python3 manage.py runserver
```

After model change, create and apply migrations
```python
$> python3 manage.py makemigrations
$> python3 manage.py migrate
```
