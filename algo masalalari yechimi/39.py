x,y = map(int,input().split(" "))
a=(x+y)/2
b=4*x*y
if y>x:
    print(f"{a:.1f}",end=(" "))
    print(f"{b:.1f}")
if x>y:
    print(f"{b:.1f}" ,end=(" "))
    print(f"{a:.1f}")