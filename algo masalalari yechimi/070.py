import math
n,x = map (int,input().split(" "))

S=0
i=1

for i in range(1,(n+1)) :
    S+=math.pow((-1),(i-1))*math.pow(x,2*i-1)/math.factorial(2*i-1)

    
print(f"{S:.3f}")