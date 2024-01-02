from math import fabs

a=float(input())
if a<0 :
	print(f"{fabs(a+1):.2f}")
else :
	print(f"{fabs(a-1):.2f}")
