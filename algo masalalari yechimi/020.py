import math
x,y = map(float,input().split(" "))
a=(y+x*y)/(math.fabs(x*y)+5)
b=(x*y+math.pow(y,2))/(math.pow(y,2)+a)
c=(math.pow(x,2)+1)/(math.pow(x,2)+b)
d=1+math.cos(x)+1/math.sin(math.fabs(x))
T11= c+1/d
print(f"{T11:.2f}")
