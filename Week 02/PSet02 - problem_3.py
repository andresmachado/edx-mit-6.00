# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 09:31:26 2016

@author: andre

# edX MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
# Problem Set 2, problem 3

# Use bisection search to make the program faster

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Problem Summary: Use bisection search to search for the smallest monthly payment
# to the cent such that we can pay off the entire balance within a year.
"""

# Test Cases, comment out before submitting for grading
#Test Case 1
balance = 320000
annualInterestRate = 0.2

monthly_interest_rate = (annualInterestRate / 12.0)
payment_lower = (balance / 12)
payment_upper = (balance * ((1 + monthly_interest_rate)**12)) / 12.0
original_balance = balance

while balance != 0.00:
    # Set value for thePayment to midpoint of lower and upper
    payment = (payment_lower + payment_upper) / 2

    # Reset balance each time through while loop
    balance = original_balance

    for i in range(1,13):
        balance = (balance - payment) * (1 + monthly_interest_rate)

    if balance > 0:
        payment_lower = payment

    elif balance < 0:  
        payment_upper = payment

    balance = round(balance, 2)

print("Lowest Payment:", round(payment,2))