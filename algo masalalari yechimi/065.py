n,x = map (int,input().split(" "))

S=0
i=1

for i in range(0,(n+1)) :
    S+=i/(x**(2*i))
    
print(f"{S:.3f}")