# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 08:57:17 2016

@author: andre
"""

balance = 4773
annualInterestRate = 0.2
lowest_payment = 0
monthly_interest_rate = annualInterestRate / 12.0
new_balance = balance

while new_balance > 0:
    lowest_payment += 10
    
    for m in range(0, 12):
        new_balance -= lowest_payment
        new_balance += (new_balance * monthly_interest_rate)
    
    if new_balance > 0:
        new_balance = balance

print("Lowest Payment: ", lowest_payment)
    
