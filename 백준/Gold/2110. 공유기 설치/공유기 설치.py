import sys
n, c = map(int, (input().split()))
array = [int(sys.stdin.readline()) for _ in range(n)]

array.sort()
start = 1
end = array[-1]-array[0]

result = 0

while start <=end:
    
    mid = (start+end)//2
    current = array[0]
    count = 1# 공유기 개수
    
    for i in range(1,len(array)):
        
        if array[i] >= mid+current:
            count +=1
            current = array[i]
    
    if count >= c:
        start = mid+1
        result =mid
    else:
        end = mid-1

print(result)
    