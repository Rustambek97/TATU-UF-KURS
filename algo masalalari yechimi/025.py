import math

a,x = map(float,input().split(" "))

v=math.sqrt(x-1)+math.sqrt(x+2)+math.log(math.sqrt(a*math.pow(x,2))+2,10)
u=math.sqrt(x+2)+math.sqrt(x+24)+math.pow(x,5)
TT=v/math.sqrt(u)
print(f"{TT:.2f}")
