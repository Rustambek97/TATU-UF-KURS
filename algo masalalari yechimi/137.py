n = int(input())
A = []
b = 0
cnt = 0
for i in range(0,n):
    a = list(map(int,input().split(" ")))
    A.append(a)
k = int(input())

for i in A:
    for j in range(0,n):
        if i[j]%k==0 :
            cnt+=1
            b+=i[j]

s = b/cnt

print(f"{s:.2f}")