from math import pow
n = int(input())
m = list(map(int, input().split(" ")))
M=int(input())
s=0
for i in range(0,n):
    if m[i]<M:
        s+=pow(m[i],2)
    
print(s)
    