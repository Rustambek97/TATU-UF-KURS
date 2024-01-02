n = int(input())
m = list(map(int,input().split(" ")))
x,y = map(int,input().split(" "))

cnt=0

for i in range(0,n):
    if x<=m[i]<=y:
        cnt+=1
a=n-cnt
print(a)