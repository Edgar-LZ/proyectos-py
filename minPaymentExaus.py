# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:44:29 2020

@author: Edgar López
"""
balance = 3329
annualInterestRate = 0.2
months = 12
def minimumPaymentCalc(balance, annualInterestRate):
    for i in range(0,int(balance),10):
        j = 0
        newbal = balance
        for j in range(months):
            unpaidBalance = newbal - i
            newbal = unpaidBalance + (annualInterestRate/12.)*unpaidBalance
            if newbal <=0:
                return i
    
            
print('Lowest Payment: '
      ,minimumPaymentCalc(balance, annualInterestRate))
        
