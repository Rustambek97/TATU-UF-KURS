import math


x,y,c,d = map(float,input().split(" "))


a=math.pow(math.sin(math.fabs(c*math.pow(y,3)+d*math.pow(x,3)-c*d)),2)
b=math.sqrt(c*math.pow(x,2)+d*math.pow(y,2)+7)
z=math.tan(x*math.pow(y,2)+math.pow(d,3))
F=math.fabs(a/b)+z
print(f"{F:.2f}")
