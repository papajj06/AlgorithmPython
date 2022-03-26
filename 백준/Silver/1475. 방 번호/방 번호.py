n = input()
result = [0]*9

for number in n:
    number = int(number)
    if number == 9:
        number = 6
    result[number]+=1

result[6] = (result[6]+1)//2
print(max(result))