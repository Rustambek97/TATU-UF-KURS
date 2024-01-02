from math import sin
n = int(input())
m = list(map(int, input().split(" ")))
s=1
b=True
for i in range(0,n):
    if m[i]%2==0:
        b=True
    elif m[i]%5==0:
        b=True
if b:
    s*=m[i]
    S=sin(s)
print(f"{S:.2f}")