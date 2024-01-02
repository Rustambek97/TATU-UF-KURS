from math import pow, cos, sin
x,y,a,b = map(int, input().split(" "))
S = 0
P = 1
SP = 0
sp = 1
for k in range(1,x+1):
    S+=(pow(k,2)+sin(k)+5)/pow(pow(k,7)+1,1/5)

for n in range(1,y+1):
    P *=(n+pow(n,1/2))/(n-pow(n+1,1/5)) 

for n in range(1,a+1):
    for i in range(1,b+1):
        sp *= (pow(i,2)+pow(n,2/i))/((sin(i)+cos(n))*pow(i,n))
    SP += sp
    sp=1

print(f"{S:.2f} {P:.2f} {SP:.2f}")