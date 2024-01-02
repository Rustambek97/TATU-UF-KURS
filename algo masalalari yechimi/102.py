n = int(input())
m = list(map(int, input().split(" ")))
a,b = map(int, input().split(" "))

k = min(m)

for i in range(0,n):
    if a-1<=i<b:
        x=m[i]/k
        print(f"{x:.1f}", end=" ")
    else:
        y=m[i]
        print(f"{y:.1f}", end=" ")