N,M= map(int,input().split(" "))
A = []
cnt = 0
b=0
for i in range(0,N):
    a = list(map(int,input().split(" ")))
    A.append(a)
x,y = map(int,input().split(" "))
for i in A:
    for j in range(0,M):
        if x<=i[j]<=y:
            b+=i[j]
            cnt+=1

s=b/cnt
print(f"{s:.2f}")