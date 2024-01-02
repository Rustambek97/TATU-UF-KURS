import math

x=float(input())

a=2*math.tan(x+2)-math.cos(x+math.pow(2,x))
b=1+math.pow(math.cos(x+2),2)
c=math.sin(math.pow(x,2))/(math.pow(x,2)+3)
AA=math.sqrt(a/b)+c
print(f"{AA:.2f}")
