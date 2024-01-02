from math import factorial
y = float(input())
A=0
B=0
for k in range(0,11):
    A+=(x**(2*k-1))/factorial(2*k+1)
    B+=(X**(2*k))/factorial(2*k)
t=A/B

def Y(y,t):
    f=(1.7*t*0.25+2*t*(1+y))/(6-t*(y*y-1))
    return(f)
F=Y(y,t)
print(f"{F:.2f}")