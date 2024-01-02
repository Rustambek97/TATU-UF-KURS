import math
n,k = map (int,input().split(" "))

S=0
i=0


for i in range(0,(n+1)) :
    S+=math.pow((-1),i)*math.pow(k,i)/math.factorial(i)

    
print(f"{S:.3f}")