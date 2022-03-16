# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 23:39:00 2022

@author: papajj06
"""

data = input()
row = int(data[1])
column = int(ord(data[0])) - int(ord('a'))+1

steps = ([2,1],[1,2],[-2,1],[-1,2],[2,-1],[1,-2],[-2,-1],[-1,-2])

result =0
for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]
    if next_row >=1 and next_column <=8 and next_row <=8 and next_column >=1:
        result +=1
        
print(result)