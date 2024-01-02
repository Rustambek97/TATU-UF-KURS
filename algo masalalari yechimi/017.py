import math

x,y = map(float,input().split(" "))
f1=(2*math.tan(x+math.pi/6))/(1/3+math.pow(math.cos(y+math.pow(x,2)),2))+math.log((math.pow(x,2)+2),2)
print(f"{f1:.2f}")


