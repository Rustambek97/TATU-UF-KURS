n = int(input())
A = []
for i in range(0,n):
    a = list(map(int,input().split(" ")))
    A.append(a)
b = []
for i in range(0,n):
    j = i
    b.append(A[i][j])
c = []
for i in range(0,n):
    j = i
    c.append(A[i][n-j-1])
    
print(max(b),min(c))