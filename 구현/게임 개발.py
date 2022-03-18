# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 12:57:29 2022

@author: papajj06
"""

n,m  = map(int,input().split())

d =[[0]*m for _ in range(n)] # 방문한 위치를 저장하기 위한 맵

x,y,direction = map(int,input().split())
d[x][y] = 1 # 현재 좌표 방문하니까 1로 처리

array = [] # 현재 맵 정보
for i in range(n):
    array.append(list(map(int,input().split())))
    
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -=1
    if direction == -1:
        direction ==3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x+dx[direction]
    ny = y+dy[direction]
    
    
    if d[nx][ny] == 0 and array[nx][ny]==0:
        d[nx][ny]=1
        x =nx
        y = ny
        count+=1
        turn_time=0
        continue
    else:
        turn_time+=1
        
    if turn_time ==4:
        nx = x-dx[direction]
        ny = y-dy[direction]
       
        
        if array[nx][ny] ==0:
             x= nx
             y=ny
        else:
            break
        turn_time=0
print(count)
            
