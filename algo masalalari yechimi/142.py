N= int(input())
A = []
for  i in range(0,N):
    a = list(map(int,input().split(" ")))
    A.append(a)

C = []
m = 0
for i in A:
    for j in range(m,N):
        C.append(i[j])
    m+=1
max_b = max(C)
min_b = min(C)
for i in C:
    print(i, end=" ")
print()
print(max_b,min_b)
