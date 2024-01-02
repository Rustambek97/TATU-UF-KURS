#ichma_ich tsiklni for bilan yechilishi
from math import *
x,y,c,d = map(int, input().split(" "))

S = 0
for a in range(1,x+1):
    S += (a*x+4)/sqrt(a+log(6))

P = 1
for a in range(1,y+1):
    P *= (a*x**2+6)/sin(a*x)

SP = 1

for i in range(1,c+1):
    T = 1 
    for j in range(1,d+1):
        T *= (i*j+y*x)/sqrt((j*x+y)**i)
    SP *= T

print("%.2f" % S,"%.2f" % P,"%.2f" % SP)