# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 23:28:59 2022

@author: papajj06
"""

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1
                
print(count)