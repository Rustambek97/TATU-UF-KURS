from math import fabs
x,y = map(float,input().split(" "))


if y<=2*x+3:
    if x<=0 and y<=-x :
        print("yes")
    elif -x/3-1/3<=y<=0:
        print("yes")
    else :
	    print("no")
else :
    print("no")