n = int(input())
m = list(map(int,input().split(" ")))
M=int(input())

s=0

for i in range(M,n):
    s+=m[i]
print(s)