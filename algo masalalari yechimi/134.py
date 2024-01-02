n,m = map(int,input().split(" "))
A = []

for i in range(0,n):
    a = list(map(int,input().split(" ")))
    A.append(a)
M = list(map(int,input().split(" ")))
A.append(M)
A.sort(reverse=True)
for i in A:
    for j in range(0,m):
        print(i[j], end=" ")
    print()

