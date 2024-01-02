from math import log, e, cos, pow, fabs
x,y,c,d = map(int,input().split(" "))
S=0
P=1
SP=0
sp=1

for a in range(1,x+1):
    S+=(4*a+6*log(a,e))/(pow(a,2)+a)

for a in range(1,y+1):
    P*=fabs(a-6*cos(a))/(pow(a,2)+pow(a,log(a,e)))
    
for k in range(1,c+1):
    for a in range(1,d+1):
        sp*=(a*k+x)/(pow(k,2)+pow(y,2))
    SP+=sp
    sp= 1
    
print(f"{S:.2f} {P:.2f} {SP:.2f}")
    