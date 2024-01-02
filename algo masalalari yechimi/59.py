from math import fabs 
x,y = map(float,input().split(" "))

if y<=-fabs(x*2)+1 and y>=fabs(x*2)-1 :
	print("yes")
else :
	print("no")