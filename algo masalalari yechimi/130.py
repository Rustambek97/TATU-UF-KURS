n,m = map(int,input().split(" "))
B_max = []
B_min = []
A=0
B = []
for i in range(0,n):
    a = list(map(int,input().split(" ")))
    for i in a:
        A += i
    B.append(A)
    A = 0
    B_max.append(max(a))
    B_min.append(min(a))
    
print(B)
print(max(B_max),min(B_min))