a,b,c = map(float,input().split(" "))

if 1<=a<=3 and 1<=b<=3 and 1<=c<=3 :
	print(a,b,c)
elif 1<=b<=3 and 1<=c<=3 :
	print(b,c)
elif 1<=c<=3 :
	print(c)
elif 1<=a<=3 and 1<=c<=3:
	print(a,c)
elif 1<=a<=3 and 1<=b<=3 :
	print(a,b)
elif 1<=a<=3 :
	print(a)
elif 1<=b<=3 :
	print(b)

	