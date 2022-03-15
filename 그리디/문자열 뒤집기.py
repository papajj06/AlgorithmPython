# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:22:59 2022

@author: papajj06
"""

s = input()
zerocount = 0
onecount = 0

if s[0]=="1":
   onecount+=1
else:
   zerocount+=1

for i in range(1,len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=="0":
            onecount+=1
        else:
            zerocount+=1

print(min(zerocount,onecount))
        
    