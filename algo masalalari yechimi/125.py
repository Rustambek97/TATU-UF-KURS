from math import pow
n = int(input())
m = list(map(int,input().split(" ")))
k,l = map(int,input().split(" "))
s=0

for i in range(k-1,l):
    s+=pow(m[i],3)
print(s)