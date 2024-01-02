from math import cos , sin,pow
a=int(input(""))

S=0
h=0.5
i=0

while  i<=10 :
    S+=a*cos(i)-sin(pow(i,2))
    i+=h
print(f"{S:.2f}")