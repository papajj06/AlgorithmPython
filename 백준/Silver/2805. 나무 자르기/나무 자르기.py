import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 0
end = max(tree)

while start <= end:
    total = 0
    mid =(start+end)//2
    
    for x in tree:
        if x > mid:
            total += x-mid
    if total < m:
        end = mid-1
    else:
        start = mid+1

print(end)