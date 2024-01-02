s = str(input())
m = list(s.split(" "))
n = []
for i in m:
    a = len(i)
    n.append(a)
id = n.index(max(n))
print(m[id])


