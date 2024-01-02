import math

a,b = map(float,input().split(" "))
x=b*(a+b)/(2*b+a*b)
y=math.pow(a,2)+math.pow(b,2)+2
T=math.pow(a,1/5)+math.pow(x,1/4)*y
print(f"{T:.2f}")
