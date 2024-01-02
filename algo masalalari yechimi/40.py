x,y,z = map(int,input().split(" "))

if x>0 and y>0 and z>0 :
	print(x**2,y**2,z**2)
elif y>0 and z>0 :
	print(x,y*y,z*z)
elif x>0 and z>0 :
	print(x*x,y,z*z)
elif x>0 and y>0 :
	print(x*x,y*y,z)
elif x>0 :
	print(x*x,y,z)
elif y>0 :
	print(x,y*y,z)
elif z>0 :
	print(x,y,z*z)
else :
	print(x,y,z)