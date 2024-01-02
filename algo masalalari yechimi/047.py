from math import fabs
a=float(input())

if a<1 :
	print(f"{fabs(a):.2f}")
elif 1<=a<2 :
	print("1.00")
else :
	print(f"{(-2*a+5):.2f}")

