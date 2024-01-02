import math

a,x = map(float,input().split(" "))

p=x*math.sin(x/2+x/3+x/4)
q=math.log(math.pow(x,2)-2,10)+math.pow(3,a)
r=math.cos(x+3)*math.sin(x+3)+8

BB1=p+q/r

print(f"{BB1:.2f}")
