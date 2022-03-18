# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 14:43:50 2022

@author: papajj06
"""

n = int(input())
a = list(map(int,input().split()))
b = list(map(int, input().split()))
s=0

for i in range(n):
    s += max(a)*min(b)
    a.pop(a.index(max(a)))
    b.pop(b.index(min(b)))

print(s)