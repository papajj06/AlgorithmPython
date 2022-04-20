import sys

number= int(input())

for i in range(0,number):
    count = 1
    people = []
    
    N = int(input())
    for i in range(N):
        paper, interview = map(int,sys.stdin.readline().split())
        people.append([paper, interview])

    people.sort() # 서류 기준 오름차순 정렬
    max_people = people[0][1]
    
    for i in range(1,N):
        if max_people > people[i][1]:
            count += 1
            max_people = people[i][1]

    print(count)