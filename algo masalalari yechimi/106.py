from math import pow
n = int(input())
m = list(map(int, input().split(" ")))

S=0
for i in range(0,n):
    S+=pow(m[i],2)
print(S)