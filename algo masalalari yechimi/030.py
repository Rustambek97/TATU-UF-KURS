import math

x,y,z = map(float,input().split(" "))
a=x+math.pow((math.fabs(y)+2),1/4)
b=math.pow(math.e,(x-1))/math.sin(z+2)+2

AF=math.pow(2,(-x))*math.sqrt(a)*math.pow(b,1/3)

print(f"{AF:.2f}")

