import math

x,y = map(int,input().split(" "))
a=math.pow(x+y,2)+math.sqrt(math.fabs(y)+2)-(x-x*y/(math.pow(x,2)/2-5))
b=math.log(math.fabs(a))
c=math.pow(math.cos(x+y),2)/math.pow((x+y),1/3)
z=b+c
print(f"{z:.2f}")
