a,b = map(float,input().split(" "))

u = min(a,b)
v = min(a*b,max(a,b))
s = min(u+v,3.14)

print(f"{u:.2f} {v:.2f} {s:.2f}")