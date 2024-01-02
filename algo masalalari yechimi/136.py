n,m = map(int,input().split(" "))
A = []

for i in range(0,n):
    a = list(map(int,input().split(" ")))
    A.append(a)
k = int(input())

for i in A:
    for j in range(0,m):
        if i[j] != i[k-1]:
            print(i[j] , end= " ")
    print()