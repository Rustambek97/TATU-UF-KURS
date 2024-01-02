from math import sin
n=int(input())

S=0
i=1
for i in range(1,(n+1)) :
    S+= sin(i)/2**i
print (f"{S:.2f}") 
