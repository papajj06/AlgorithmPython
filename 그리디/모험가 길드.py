# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 21:43:46 2022

@author: papajj06
"""

n = int(input())
data = list(map(int,input().split()))
data.sort()
count = 0
result = 0
for i in data:
    count += 1
    if count >= i:
        result +=1
        count = 0

print(result)

