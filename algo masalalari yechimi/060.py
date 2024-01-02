from math import fabs 
x,y = map(float,input().split(" "))
if x>=fabs(y/2)-2 and x<=0 :
	print("yes")
elif x>=0 and x*x+y*y<=1 :
	print("yes")
else :
	print("no")