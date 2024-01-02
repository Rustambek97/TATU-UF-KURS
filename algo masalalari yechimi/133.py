n = int(input())
m1 = []
for i in range(0,n):
    a = list(map(int, input().split(" ")))
    m1.append(a)

m2 = []
for i in range(0,n):
    a = list(map(int, input().split(" ")))
    m2.append(a)
    
M = []
for i in range(0,n):
    b = []
    for j in range(0,n):
        b.append(m1[i][j])
    for j in range(0,n):
        b.append(m2[i][j]) 
    
    M.append(b)
    

for i in range(0,n):
    for j in range(0,2*n):
        print(M[i][j], end=" ")
    print()
    