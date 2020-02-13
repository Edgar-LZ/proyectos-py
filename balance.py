# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:15:16 2020

@author: Edgar López
"""
balance = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
months = 12
payment_rate= .15
for i in range(months):
    unpaidBalance = balance - payment_rate*balance
    balance = unpaidBalance + (annualInterestRate/12.)*unpaidBalance
    #print('Month '+str(i+1) +' Remaining balance:',round(balance,2))

print('Remaining balance: ',round(balance,2))
