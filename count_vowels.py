# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:51:43 2020

@author: Edgar López
"""
s = 'azcbobobegghakaeioul'
vowels = 'aeiou'
count = 0 
for letter in s:
    if letter in vowels:
        count += 1
        
print('Number of vowels: '+str(count))
