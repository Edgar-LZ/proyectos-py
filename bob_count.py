# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:00:48 2020

@author: Edgar López
"""

s = 'azcbobobegghaklbobobob'
bobs = 0
for a in range(len(s)-2):
    if s[a] == 'b' and s[a:a+3] == 'bob':
        bobs +=1
print('Number of times bob occurs is: '+str(bobs))