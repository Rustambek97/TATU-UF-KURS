s = str(input())
a,b = map(int,input().split(" "))
m = list(s)
n = []
if b>a :
    for i in range(a-1,b):
        n.append(m[i])
        
    for i in n:
        print(i , end="")
else:
    for i in range(b-1,a):
        n.append(m[i])
    N = n[::-1]
    for i in N :
        print(i , end="")
    