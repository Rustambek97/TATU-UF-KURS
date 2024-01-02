t,s = map(float,input().split(" "))
def G(a,b):
    A=a*a+b*b
    B=(a+b)**2+2*b*b+4
    f=A/B
    return(f)
F=G(1.2,s)+G(t,s)+G(2*s-1,s*t)
print(f"{F:.2f}")