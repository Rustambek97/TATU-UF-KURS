from math import log ,e
n = int(input())
m = list(map(int, input().split(" ")))
M=int(input())
s=1
for i in range(0,n):
    if m[i]>M:
        s*=m[i]
    a=log(s,e)
print(f"{a:.2f}")
    