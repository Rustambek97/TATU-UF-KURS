
n = int(input())
m = list(map(int, input().split(" ")))

s=0
for i in range(0,n,2):
    s+=m[i]
    
print(s)
    
        
    
    