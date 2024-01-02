N,M= map(int,input().split(" "))
A = []
s = 0
for  i in range(0,N):
    a = list(map(int,input().split(" ")))
    A.append(a)


for  i in A:
    for j in range(0,M):
        print(i[j] ,end=" ")
    print()

