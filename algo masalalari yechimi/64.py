from math import pow 

n,x = map(int,input().split(" "))
S=0
i=1

while i in range(1,(n+1)) :
    S+=pow((-1),(i-1))/pow(x,2*i)
    i+=1
   
print(f"{S:.3f}")


