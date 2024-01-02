from math import pow
a,b,c = map(int,input().split(" "))

S=0
h=2
for i in range(a,b+1,h):
    S+=(pow(a,b)+pow(b,i)+pow(c,a))/(2*pow(i,2)+3*pow(a,i))
print(f"{S:.2f}")