import math 
a,b,c,d = map(int,input().split(" "))
S=0
i=d
h=1.5
while i<=c:
    S+=math.pow((a*i+b)/(math.pow(b,2)+math.pow(math.cos(i),2)),1/5)-math.sin(math.pow(i,2))/(a*b)
    i+=h
print((f"{S:.2f}"))