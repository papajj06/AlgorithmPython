import math
test_case = int(input())
results = []


for _ in range(test_case):
    count = 0
    x1,y1,x2,y2 = map(int,input().split())
    planet = int(input())
    
    for _ in range(planet):
        cx,cy,r = map(int,input().split())
        d1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        d2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        
        if d1 < r or d2 < r:
            
            if d1 <r and d2 <r:
                pass
            else:
                count +=1
    results.append(count)

for result in results :
    print(result)