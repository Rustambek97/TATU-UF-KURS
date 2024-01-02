n = int(input())
m = list(map(int, input().split(" ")))
k,l = map(int, input().split(" "))
SS=0
S=0
a=n-(l-k+1)
for i in range(0,n):
    SS+=m[i]

for i in range(k-1,l):
    S+=m[i]
b=(SS-S)/a
print(f"{b:.2f}")