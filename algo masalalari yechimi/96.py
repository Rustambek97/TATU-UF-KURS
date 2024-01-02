from math import pow, log, e, fabs
x,y,c,d = map(int, input().split(" "))
S = 0
P = 1
SP = 1
sp = 0
for k in range(1,x+1):
    S+= pow(-1,k)*(k+1)/(pow(k,3)+pow(k,2)+1)

for i in range(1,y+1):
    A=pow(i,3)+fabs(i-9)
    B=log(i,e)+7*i
    P *= A/B

for n in range(1,c+1):
    for m in range(1,d+1):
        a=pow(-1,m)*log(m+5,e)
        b=pow(m,n+3)+n*m
        sp += a/b
    SP *= sp
    sp=0
print(f"{S:.2f} {P:.2f} {SP:.2f}")
