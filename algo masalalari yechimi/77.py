from math import pow, sin, cos
a,b,c,d = map(int,input().split(" "))

S=0
h=2

for i in range(c,d+1,h):
    S+=pow((sin(a*i)+pow(b,2*c))/(pow(b,2)+pow(cos(i),2)),1/3)-sin(pow(i,2))/(a*b)
print(f"{S:.2f}")