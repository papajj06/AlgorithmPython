people = [int(input()) for i in range(9)]

result = sum(people)

for i in range(9):
    for j in range(i+1,9):
        if 100 == result - (people[i]+people[j]):
            a , b = people[i], people[j]
            
            people.remove(a)
            people.remove(b)
            people.sort()
            
            for i in range(len(people)):
                print(people[i])
            break
    
    
    if len(people)<9:
        break
    