from collections import deque
def dfs(v):
    visit1[v] = True
    print(v,end=" ")
    for i in range(1,n+1):
        if not visit1[i] and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visit2[v]= True
    
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(1,n+1):
            if not visit2[i] and graph[v][i] ==1:
                queue.append(i)
                visit2[i]=True

n,m,v = map(int,input().split())

graph=[[0]*(n+1) for _ in range(n+1)] 
visit1 = [False]*(n+1)
visit2 = [False]*(n+1)


for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)