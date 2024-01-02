#algo 77-masala yechilishi:
#for bilan yechilishi
from math import sin, cos
a,b,c,d = map(int,input().split(" "))

y = 0
for x in range(c,d+1,2):
    y1 = sin(a*x)+b**(2*c)
    y2 = b**2+cos(x)**2
    y3 = sin(x**2)/(a*b)
    y += (y1/y2)(1/3)-y3

print("%.2f" % y)

#while bilan yechilishi

from math import sin, cos
a,b,c,d = map(int,input().split(" "))

y = 0
x = c
while x<=d:
    y1 = sin(a*x)+b**(2*c)
    y2 = b**2+cos(x)**2
    y3 = sin(x**2)/(a*b)
    y += (y1/y2)(1/3)-y3
    x += 2

print("%.2f" % y)

