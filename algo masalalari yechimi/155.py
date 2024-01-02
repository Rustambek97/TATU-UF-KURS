n=str(input())
m=list(n.split(" "))
cnt=0
for i in m:
    if i[0] == i[0].upper():
        cnt+=1
print(cnt)