n = int(input())
m = list(map(int, input().split(" ")))
k,l = map(int, input().split(" "))

S=0
for i in range(k-1,l):
    S+=m[i]
a=S/(l-k+1)
print(f"{a:.1f}")