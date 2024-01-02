from math import fabs

a,b,c = map(int,input().split(" "))

if c<=b and b<=a:
	print(2*a,2*b,2*c)
else: 
	print(fabs(a),fabs(b),fabs(c))