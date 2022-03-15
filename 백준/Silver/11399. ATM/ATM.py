n = int(input())
time = list(map(int,input().split()))
time.sort()

result = 0

for i in range(n):
    for j in range(i+1):
        result+=time[j]
print(result)