# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 14:22:59 2022

@author: papajj06
"""

#caseA

n,m = map(int,input().split())
number = list(map(int,input().split()))
count=0

for i in range(n):
    for j in range(i+1,n):
        if int(number[i]) != int(number[j]):
            count+=1
        else:
            continue

print(count)


#caseB

n,m = map(int,input().split())
number = list(map(int,input().split()))

array = [0]*11
for x in number:
    array[x]+=1

result = 0
for i in range(1,m+1):
    n -= array[i] # A가 선택할 수 있는 개수 제외
    result += array[i]*n #A가 선택한거 외에 B가 선택할 수 있는 개수

print(result)