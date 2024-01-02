import math 
n=int(input())

S=0
i=1
for i in range(1,(n+1)) :
    S+= math.pow((-1),(i-1))*math.sin(math.pow(i,i))/math.pow(2,i)
print (f"{S:.2f}") 
