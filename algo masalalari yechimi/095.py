from math import pow, e, fabs
x,y,c,d = map(int, input().split(" "))
S = 0
P = 0
SP = 0
sp = 1
for i in range(1,x+1):
    S+= (pow(i,4)+pow(i,2)+3)/(pow(i+pow(e,i),0.5))

for k in range(1,y+1):
    P += (k+1)/(pow(k,3)+5*k)

for m in range(1,c+1):
    for n in range(1,d+1):
        A=fabs(pow(m,n)-pow(n,m))
        B=pow(m,n)+pow(n,m)
        sp *= pow(A/B,0.5)
    SP += sp
    sp=1

print(f"{S:.2f} {P:.2f} {SP:.2f}")
