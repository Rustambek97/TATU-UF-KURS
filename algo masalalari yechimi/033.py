from math import pow
x,y,z = map(float,input().split(" "))
a=pow(min(x+y/2,x,y,z),2)
b=max(x+y+z,x,y,z)
print(f"{b:.2f}")
print(f"{a:.2f}")