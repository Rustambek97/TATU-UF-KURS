n = int(input())
m = list(map(int, input().split(" ")))
s=1
ss=0
for i in range(0,n,2):
    s*=m[i]
for i in range(1,n,2):
    ss+=m[i]
a=s/ss

print(f"{a:.2f}")
