# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:34:23 2016

@author: andre
"""

balance = 42
minimum_monthly_payment_rate = 0.04
anual_interest_rate = 0.2


def calculate_remanining_payment(balance):
    for n in range(1, 13):
        monthly_interest_rate = anual_interest_rate / 12.0
        minimum_monthly_payment = minimum_monthly_payment_rate * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        new_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        balance = new_balance
    print("Remaining balance:".format(n), round(new_balance,2))

calculate_remanining_payment(balance)