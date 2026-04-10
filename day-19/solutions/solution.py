# Day 19 - OOP Basics | SOLUTION
# Try to solve exercises.py yourself before looking here!

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
    def __str__(self):
        return f'Account({self.owner}: ${self.balance})'
acc = BankAccount('Mostafa', 1000)
acc.deposit(500)
print(acc)
