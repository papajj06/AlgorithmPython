# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:27:58 2022

@author: papajj06
"""

num = int(input())
money =list(map(int,input().split()))

target = 1  #최소값 1을 타깃으로
money.sort()
for i in money:
    if target<i:
        break
    target+=i
print(target)