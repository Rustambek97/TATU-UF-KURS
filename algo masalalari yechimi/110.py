n = int(input())
m = list(map(int, input().split(" ")))
K,M = map(int, input().split(" "))
S = 1
for i in range(0,n):
    if m[i]==K:
        S *= K
    elif m[i]==M:
        S *= M
    
print(S)       

