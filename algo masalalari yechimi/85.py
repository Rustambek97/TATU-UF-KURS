from math import pow
a,b,c = map(int,input().split(" "))
S=0

for i in range(1,21,5):
    S+=(pow(i,2)*a+b*i+c)/(pow(a,2)+pow(b,2)+pow(i,2))
print(f"{S:.2f}")