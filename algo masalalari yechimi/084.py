from math import pow,sin,cos
a,b,c = map(int,input().split(" "))
S=0
i=-1
h=0.25
while i<=1:
    S+=pow((sin(a*i)+pow(b,c))/(pow(b,2)+pow(cos(i),2)),1/3)-sin(pow(i,2))/(a*b)
    i+=h
print(f"{S:.2f}")