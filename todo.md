# Budget Planner TODO and musings

## Introduction
This really needs a better name.
The scope of this app is learning about going live with a real application that serves a frontend, has a backend and manages data in its own database.

## To-Dos
- [] Page to modify categories
    - [] Simple form to save new category
    - [] Show list of existing icons by mapping of icon font character and name in model's CATEGORY_ICON_CHOICES list
- [] Sort transactions of account by date
- [] Apply filters to sorted transactions for a given date range
- [] 


## Features & UseCases
The application should help managing the budget and generally get a better understanding of the spendings of the household.
The following is a attempt to describe the planned features of the app. For this I try to represent each feature as a user story. This way, one can hope to at least add some automatic testing, later.

'It' here always refers to the app.

### Basics
- It should offer a way of managing bank accounts:
    - Creating
    - Deleting
    - It should be possible to select 1-n users as owners for each account
    - Change details
- It should be possible to globally add categories for transactions. Those are not tied to a specific account. These are for later grouping transactions together for analysis.
    - It should be possible to globally delete categories.
    - It should be possible to globally edit categories.
- It should be possible to add a transaction to a specific account.
    - A transaction can either be of type "spending" or "earning"
    - It should be possible to specify that a transaction is repeated every 
        - month
        - year
    - It should be possible to add a category to each transaction.
    - It should be possible to edit a transaction, after it was created.

### Representation
- A overview of all accounts should exist.
    - On this page, new accounts can be added, or existing ones edited or deleted.
- A overview of all transactions in a account should exist.
    - On this page, new transactions can be added, or existing ones edited or deleted.
- A quick entry-form for new transaction should exist
- A overview of all categories should exist.
    - On this page, new categories can be added, and existing ones edited or deleted.
    - The category overview should show all categories. 
    - it should offer a view to show the sum of transactions with a single category, by week, month and year.
    - it should offer a view to show the sum of all transactions sorted by categories. There should be a way of comparing these.

### Workflows
- A user should be able to log in to the app, using his username and password.
- The account overview should show all accounts and their balances.

### Class sketches
Those have been sacked in favour of the already done class models for the database. See savings/models.py