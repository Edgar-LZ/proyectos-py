# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:21:13 2020

@author: Edgar López
"""

s = 'zyxwvutsrqponmlkjihgfedcba'
print('Given string: ' + s)

prechar = s[0]
subs1 = s[0]
subs2 = ''

for char in s[1:len(s)+1]:
#    print('char',char, 'pre', prechar, 'sub1', subs1, 'sub2', subs2)
    if char >= prechar:
        subs1 += char
        prechar = char
        
        #print(subs1)
    else:
        prechar = char
        if len(subs1) > len(subs2):
            subs2 = subs1
            subs1 = char
            #print(subs2)
            continue
        #if len(subs1) == len(subs2):
        subs1 = prechar
if len(subs2) >= len(subs1):    
    print('Longest substring in alphabetical order is: '+subs2)
else:
    print('Longest substring in alphabetical order is: '+subs1)