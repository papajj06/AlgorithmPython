# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:59:15 2022

@author: papajj06
"""

number = input()
sum=0
length= len(number)
number_front = number[ :len(number)//2]
number_back = number[len(number)//2 : ]

for i in range(length//2):
    sum+=int(number[i])

for i in range(length//2,length):
    sum -=int(number[i])

if sum==0:
    print("Lucky")
else:
    print("Ready")
    