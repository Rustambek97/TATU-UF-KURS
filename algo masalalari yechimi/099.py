from math import e, pow
x,y,c,d = map(int,input().split(" "))
S=0
P=1
SP=0
sp=1

for k in range(1,x+1):
    S+=pow(k,3)+pow(e,k)

for a in range(3,y+1):
    P*=a*x/pow(pow(a,2)+pow(x,2),0.5)
    
for i in range(1,c+1):
    for j in range(1,d+1):
        sp*=(i*x+pow(j,2))/pow(pow(i,2)+j*y,0.5)
    SP+=sp
    sp= 1
    
print(f"{S:.2f} {P:.2f} {SP:.2f}")
    