n=int(input())
m=list(map(int,input().split(" ")))
s=0

for i in range(1,n,2):
    s+=m[i]
    
for i in range(0,n):
    if m[i]%2==1 and m[i]>0:
        m[i]=m[i]/s
for i in range(0,n):
    print(f"{m[i]:.2f}",end=" ")

        