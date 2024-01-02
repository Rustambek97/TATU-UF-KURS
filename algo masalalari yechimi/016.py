import math

x,y = map(float,input().split(" "))

a=(math.pow(y,2)+2)/(x+math.pow(x,3)/5)
c1=(x+y)/(math.pow(y,2)+math.fabs(a))+math.pow(math.e,(y+2))
print(f"{c1:.2f}")
