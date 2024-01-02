
n = int(input())
m = list(map(int, input().split(" ")))
S=0

for i in range(0,n):
    if m[i]%2==0 or m[i]%5==0 or m[i]%3==0:
        S += m[i]
    
    
    
print(S)