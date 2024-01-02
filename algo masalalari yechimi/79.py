from math import cos , pi,pow
a=int(input(""))

S=0
h=pi/19
i=-pi/2

while  i<=pi :
    S+=pow(a,a/3)+pow(i,2)*cos(a*i)
    i+=h
print(f"{S:.2f}")