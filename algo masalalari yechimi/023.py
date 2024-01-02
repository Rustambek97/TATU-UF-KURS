from math import pow,cos,fabs

a,b,c,d,x = map(float,input().split(" "))

A=a*pow(x,2)+b*x+c
if a==0:
    B=x*pow(a,3)+pow(a,2)
else:
    B=x*pow(a,3)+pow(a,2)+a**(b-c)
    
C=cos(fabs((a*x+b)/(c*x+d+pow(2,c))))
if B==0 :
    y2=C
else:
    y2=A/B+C
print(f"{y2:.2f}")

