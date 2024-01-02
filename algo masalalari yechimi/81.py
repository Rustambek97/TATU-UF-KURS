from math import cos , sin,pow
a,b = map(int,input().split(" "))

S=0


for i in range(1,13,2) :
    S+=pow(a,2)+pow((b+sin(i))/(pow(a,3)+pow(cos(pow(i,3)),2)),1/5)

print(f"{S:.2f}")