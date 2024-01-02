import math

a,x,y = map(float,input().split(" "))
m=math.pow(math.e,(x*y))-x*math.sin(a*x)-(math.pow(x,2)+2)/(math.fabs(x)+5)
n=math.log(math.pow(x,2)+2,math.e)+5
W2=math.sqrt(m)+math.sqrt(n)
print(f"{W2:.2f}")

