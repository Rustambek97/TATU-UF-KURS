import math
n=int(input())
S=0
i=0

for i in range(1,n+1) :
    S += math.pow(-1,i-1)/math.factorial(2*i-1)
print(f"{S:.4f}")