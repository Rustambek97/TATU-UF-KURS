from math import pi , pow
h,r = map(int,input().split(" "))
s=pi*pow(r,2)*h/3
print(f"{s:.2f}")
