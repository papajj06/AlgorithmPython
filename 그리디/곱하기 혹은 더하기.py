# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 22:45:54 2022

@author: papajj06
"""

s = input()
result = int(s[0])
for i in range(1,len(s)):
    num = int(s[i])
    if num>=0 or num<=1:
        result+=num
    else :
        result*=num
print(result)
    
        