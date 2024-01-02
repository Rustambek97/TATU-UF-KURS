from math import e, pow, sin, log
x,y,c,d = map(int,input().split(" "))
S=0
P=1
SP=1
sp=1

for a in range(1,x+1):
    S+=(a*x+4)/pow(a+log(6,e),0.5)

for a in range(1,y+1):
    P*=(a*pow(x,2)+6)/sin(a*x)
    
for i in range(1,c+1):
    for j in range(1,d+1):
        sp*=(i*j+x*y)/pow(x*j+y,i/2)
    SP*=sp
    sp= 1
    
print(f"{S:.2f} {P:.2f} {SP:.2f}")
    