import sys
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
tomato=[list(map(int,input().split())) for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(li):
    q=deque()
    for i in li:
        q.append(i)
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not(0 <= nx < n and 0 <= ny < m):
                continue
            if tomato[nx][ny]==-1:
                continue
            if tomato[nx][ny]==0: #방문안한토마토라고 생각하자
                q.append((nx,ny))
                tomato[nx][ny]=tomato[x][y]+1

li=[]
for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            li.append((i,j))
bfs(li)

def result(): #bfs후에도 토마토배열에 0이 남아있으면 -1을 출력
    anwser=0
    for i in range(n):
        for j in range(m):
            if tomato[i][j]==0:
                return print(-1)
            anwser=max(anwser,tomato[i][j])
    return print(anwser-1)

result()