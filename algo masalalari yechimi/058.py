x,y = map(float,input().split(" "))

if x*x+y*y<=1 and y<=x/2 :
	print("yes")
else :
	print("no")