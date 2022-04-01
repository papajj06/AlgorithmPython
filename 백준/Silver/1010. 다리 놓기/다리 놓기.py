T = int(input())
ass=[1,1]
def fact(a):
    if len(ass)-1<a:
        for i in range(len(ass), a+1):
            ass.append(ass[-1]*len(ass))
    return ass[a]
for _ in range(T):
    N, M = map(int, input().split())
    print(round(fact(M)/(fact(M-N)*fact(N))))