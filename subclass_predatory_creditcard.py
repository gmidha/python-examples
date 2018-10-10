#!/usr/bin/env python3

# This program demonstrates the usage of Inheritance in python. We are going to extend the functionality of CreditCard class present in class_creditcard.py

from class_creditcard import CreditCard

class PredatoryCreditCard(CreditCard):

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
            return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor

def main():
    p = PredatoryCreditCard('Tiny','BankofWealth','102', 1000,3)
    p.charge(200)
    print(p.get_balance())
    p.process_month()
    print(p.get_balance())

if __name__ == "__main__":
    main()
