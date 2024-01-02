import math
n,x = map (int,input().split(" "))

S=0
i=1

for i in range(1,(n+1)) :
    S+=math.pow(-1,i)*math.pow(x,i)/math.factorial(i)

    
print(f"{S:.3f}")