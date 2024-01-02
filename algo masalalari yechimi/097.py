from math import pow, fabs, e, sin
x,y,c,d = map(int,input().split(" "))
S=0
P=1
SP=0
sp=1
for n in range(1,x+1):
    S+=1/(5-17*n+pow(n,3))
    
for m in range(1,y+1):
    P*=pow(fabs(m-5)+1,0.5)/(pow(m,2)+4*m-1)
    
for i in range(1,c+1):
    for k in range(1,d+1):
        sp*=pow(-1,i)*pow(fabs(sin(k)+pow(e,k)),1/7)/(2*fabs(4*pow(i,3)-pow(k,4)))
    SP+=sp
    sp=1
print(f"{S:.2f} {P:.2f} {SP:.2f}")