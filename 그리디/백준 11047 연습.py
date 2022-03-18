# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 23:53:44 2022

@author: papajj06
"""

n,k = map(int,input().split())
money_type=[]

for i in range(n):
    money_type.append(int(input()))

count = 0

for i in range(n-1,-1,-1):
    if k==0:
        break
    if k < money_type[i]:
        continue
    else:
        count += k//money_type[i]
        k%= money_type[i]
print(count)