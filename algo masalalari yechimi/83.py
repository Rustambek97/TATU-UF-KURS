from math import pow
a,b,c = map(int,input().split(" "))
S=0
i=5
h=0.5
while i<=10:
    S+=(pow(a,2)+b*i+pow(i,c))/(pow(a,2)+pow(b,2)+pow(i,2))
    i+=h
print(f"{S:.2f}")