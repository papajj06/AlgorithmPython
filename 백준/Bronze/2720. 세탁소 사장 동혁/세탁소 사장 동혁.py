T = int(input())

for _ in range(T):
    money = int(input())        
    coin = {25: 0, 10: 0, 5: 0, 1: 0}
    
    while money:
        for num in [25, 10, 5, 1]:
            while money >= num:
                money -= num
                coin[num] += 1
                
    print(coin[25], coin[10], coin[5], coin[1]) 