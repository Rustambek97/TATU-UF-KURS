n = int(input())
s = str(input())
m = list(s)

for i in m:
    if i == "$":
        m.remove("$")
for i in m:
    print(i , end="")
        