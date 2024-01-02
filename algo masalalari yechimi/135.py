n,m = map(int,input().split(" "))
A = []

for i in range(0,n):
    a = list(map(int,input().split(" ")))
    A.append(a)
k = int(input())

for i in A:
    if i!=A[k-1]:
        for j in range(0, m):
            print(i[j], end=" ")
        print()