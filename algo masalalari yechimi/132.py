L = int(input())

a = list(map(int, input().split(" ")))

n,m = map(int, input().split(" "))

M = []

for i in range(0,n):
    b = []
    for j in range(0,m):
        if bool(a):
            b.append(a.pop(0))
        else:
            b.append(0)
    M.append(b)

for i in range(0,n):
    for j in range(0,m):
        print(M[i][j], end=" ")
    print()