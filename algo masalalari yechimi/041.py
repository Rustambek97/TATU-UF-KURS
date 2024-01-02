x,y,z = map(float,input().split(" "))

if x<y<z<1 :
	print((y+z)/2,y,z)
elif x<z<y<1 :
	print((y+z)/2,y,z)
elif y<x<z<1 :
	print(x,(x+z)/2,z)
elif y<z<x<1 :
	print(x,(x+z)/2,z)
elif z<y<x<1 :
	print(x,y,(x+y)/2)
elif z<x<y<1 :
	print(x,y,(x+y)/2)
else :
	print(x,y,z)
