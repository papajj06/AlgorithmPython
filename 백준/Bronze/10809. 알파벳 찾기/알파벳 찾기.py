number= input()
check = [-1]*26
 
for i in range(len(number)):
    if check[ord(number[i])-97] != -1:
        continue
    else:
        check[ord(number[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')