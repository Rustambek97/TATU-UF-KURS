from math import sin , fabs
t,s = map(float,input().split(" "))
def f(a,b,c):
    A=2*a-b-sin(c)
    B=5+fabs(c)
    F=A/B
    return(F)
ff=f(t,-2*s,1.17)+f(2.2,t,s-t)
print(f"{ff:.2f}")