from math import pow
n = int(input())
m = list(map(int,input().split(" ")))
s=0
ss=0
for i in range(0,n):
    ss+=m[i]
    s+=pow(m[i],2)
a=ss/n
print(s)
print(f"{a:.2f}")
    