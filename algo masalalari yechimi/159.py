n=str(input())
m=list(n.split(" "))
cnt=0
for i in m:
    if i[0]=="a" and i[-1]=="b":
        cnt+=1
print(cnt)