import math

a,b,c,x = map(float,input().split(" "))

t=math.sqrt(math.fabs(math.pow(x,3)+3*x)+math.cos(x-2))
v=a/4+b/3+c/2+1
W1=0.75+(8.2*math.pow(x,2)+t)/v
print(f"{W1:.2f}")

