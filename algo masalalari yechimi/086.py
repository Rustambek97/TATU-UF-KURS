from math import pow,sin,cos
a,b,c = map(int,input().split(" "))
S=0
i=c
h=0.25
while i<=b:
    S+=pow(a,2)*cos(i)+sin(i)/2+b*pow(i,2)
    i+=h
print(f"{S:.2f}")