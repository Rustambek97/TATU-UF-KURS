from math import pow, e, log, cos
x,y,a,b = map(int, input().split(" "))
S = 0
P = 1
SP = 0
sp = 1
for m in range(1,x+1):
    S+=(pow(m,2)+2*m)/(pow(m,3)+m*pow(cos(m),2)+1)

for i in range(1,y+1):
    P *= (pow(i,2)+1)/(pow(i,3/i)+2)


for n in range(1,a+1):
    for k in range(1,b+1):
        sp *= log((pow(k,n)+pow(k,1/n))/(pow(k,3)+pow(n,1/k)),e)
    SP += sp
    sp=1

print(f"{S:.2f} {P:.2f} {SP:.2f}")
