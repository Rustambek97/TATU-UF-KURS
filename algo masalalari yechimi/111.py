
n = int(input())
m = list(map(int, input().split(" ")))
M=int(input())
s=0
for i in range(0,n):
    if m[i]>M:
        s+=m[i]
    
print(f"{s:.2f}")
    