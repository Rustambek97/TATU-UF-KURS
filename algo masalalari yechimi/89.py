import math 
a,b,c = map(int,input().split(" "))
S=0
i=0
h=0.25
while i<=1:
    S+=math.pow((math.sin(a*i)+math.pow(b,c))/(math.pow(b,2)+math.pow(math.cos(i),2)),1/2)-math.sin(math.pow(i,2))/(a*b)

    i+=h
print((f"{S:.2f}"))