from math import pow,sin,cos,pi
a= int(input())
S=0
i=-pi/2
h=pi/10
while i<=pi:
    S+=2*pow(a,sin(2*i)/3)+pow(i,2)*cos(a*i)
    i+=h
print(f"{S:.2f}")