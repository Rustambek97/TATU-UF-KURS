a,b,c = map(float,input().split(" "))

A=max(a,a+b)+max(a,b+c)
B=1+max(a+b*c,1.15)
C=A/B
print(f"{C:.2f}")