from math import pow, e, log
a,b,c,d = map(int, input().split(" "))
S = 0
P = 1
SP = 0
for m in range(1,a+1):
    A = 3*pow(m,3)+4*m+5
    B = pow(m,3)+log(m,e)
    S += A/B

for k in range(1,b+1):
    P *= k/(pow(k,3)+7*k+5)

sp = 1
for i in range(1,c+1):
    for m in range(1,d+1):
        sp *= (log(i,e)+pow(m,i))/pow(m,i)
    SP += sp
    sp=1

print(f"{S:.2f} {P:.2f} {SP:.2f}")