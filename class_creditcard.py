#!/usr/bin/env python3

# This program contains CreditCard class and demonstrates a simple class example

class CreditCard:

    def __init__(self, customer, bank, acnt, limit):

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_accnt(self):
        return self._accnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return false
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount

def main():
    c = CreditCard('Jim', 'BankofMoney', '101', 1000)
    print(c.get_balance())
    c.charge(100)
    print(c.get_balance())
    c.make_payment(10)
    print(c.get_balance())

if __name__ == "__main__":
    main()
