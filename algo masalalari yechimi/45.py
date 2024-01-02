from math import sqrt
a,b,c = map(int,input().split(" "))

D=b*b-4*a*c

if D<0:
    print("NO")
else:
    x1=(-b+sqrt(D))/(2*a)
    x2=(-b-sqrt(D))/(2*a)
    print(f"{x1:.2f}" , end=" ")
    print(f"{x2:.2f}")