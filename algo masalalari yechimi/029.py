import math

a,x,y = map(float,input().split(" "))
t=math.pow(math.e,x)+a/(math.pow(x,2)+2)
v=math.pow(y,2)+math.pow(math.e,x)+math.sqrt(t)+math.pow(math.cos(x),2)/math.sin(math.pow(x,2))

TT=math.sqrt(v)+math.pow(math.cos(x),3)

print(f"{TT:.2f}")
