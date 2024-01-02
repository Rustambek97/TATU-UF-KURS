N,M= map(int,input().split(" "))
A = []
for  i in range(0,N):
    a = list(map(int,input().split(" ")))
    A.append(a)
k = 0
for i in A:
    for j in range(0,M):
        if i[j]<0 :
            k+=j

for i in A:
    for j in range(0,M):
        if j!=k :
            print(i[j] , end=" ")
    print()


