from math import pow, cos, sin
a,b,c = map(int,input().split(" "))
h=3
S=0

for i in range(a,c+1,h):
    S+=pow((a*i+b)/(pow(b,2)+pow(cos(i),2)),1/3)-sin(pow(i,2))/(a*b)
print(f"{S:.2f}")
