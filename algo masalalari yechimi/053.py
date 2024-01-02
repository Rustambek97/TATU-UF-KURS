from math import fabs
x,y = map(float,input().split(" "))


if -2<=x<=2 and y<=1.5 and y>=1 :
	print("yes")
elif -1<=x<=1 and fabs(x)<=y:
    print("yes")
else :
	print("no")