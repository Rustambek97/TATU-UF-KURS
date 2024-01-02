s,t = map(float,input().split(" "))

def h(a,b):
    f=a/(b*b+1)+b/(a*a+1)-(a-b)**3
    return(f)
F=h(s,t)+max(h(s-t,s*t),h(s-t,s+t))+h(1,1)
print(f"{F:.2f}")