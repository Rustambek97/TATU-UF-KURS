import math

x,y = map(float,input().split(" "))
a=1/(x+2/math.pow(x,2)+3/math.pow(x,3))+math.pow(math.e,(math.pow(x,2)+3*x))
b=math.atan(x+y)+math.pow(math.fabs(x+5),2)
c=math.pow(math.cos(math.pow(y,2)+math.pow(x,2)/2),2)
f2=a/b-c
print(f"{f2:.2f}")
