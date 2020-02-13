# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 16:26:14 2020

@author: Edgar López

Using the bysection method, finds the minumum monthly payment needed
to completly pay a balance in one year
"""
balance = 320000
annualInterestRate = 0.2
lower = balance/12
upper = (balance/12.)*(1+annualInterestRate)**12


def balanceCalc(balance, annualInterestRate, monthlyPayment):
    """
    Calculates the final balance after one year of paying
    monthlyPayment every month.
    """
    months = 12
    for i in range(months):
    #    print('Month '+str(i+1) +' Remaining balance:',round(balance,2))
        unpaidBalance = balance - monthlyPayment
        balance = unpaidBalance + (annualInterestRate/12.)*unpaidBalance
    return balance


def bisectionMinPayment(low, up,balance, annualInterestRate):
    """
    Uses bisection method to calculate the minimum monthly payment needed
    to compleatly pay a debt in one year.
    """
    monthlyPaymentRate = (low+up)/2.
    epsilon = 0.001
    a = balanceCalc(balance, annualInterestRate, monthlyPaymentRate)
    while abs(a) - epsilon > 0:
        if a > 0:
            low = monthlyPaymentRate
            monthlyPaymentRate = (low+up)/2.
            a = balanceCalc(balance, annualInterestRate, monthlyPaymentRate)
        else:
            up = monthlyPaymentRate
            monthlyPaymentRate = (low+up)/2.
            a = balanceCalc(balance, annualInterestRate, monthlyPaymentRate)
            
    return round(monthlyPaymentRate,2)

print('Lowest Payment: ',
      bisectionMinPayment(lower, upper,balance, annualInterestRate))
