from math import fabs
x,y = map(float,input().split(" "))

if x>=-1 and x<=1 and y<=fabs(x) and y>=-2 :
	print("yes")
else :
	print("no")
