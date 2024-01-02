
n = int(input())
m = list(map(int, input().split(" ")))
a=max(m)

for i in range(0,n):
    b=m[i]/a
    
    print(f"{b:.2f}")
    
        
    
    