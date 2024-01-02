from math import pow
n = int(input())
m = list(map(int,input().split(" ")))
s=0
S=0
cnt=0
for i in range(0,n):
    if m[i]%2==0:
        s+=m[i]
        cnt+=1
S=s/cnt
print(f"{S:.2f}")
        
    