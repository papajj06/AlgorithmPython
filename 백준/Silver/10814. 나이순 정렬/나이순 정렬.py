n = int(input())

people = []

for i in range(n):
    data = input().split()
    people.append((int(data[0]),data[1]))
    
people = sorted(people, key=lambda name: name[0])
for name in people:
    print(name[0], name[1])