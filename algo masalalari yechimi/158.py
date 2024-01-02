n=str(input())
m=list(n.split(" "))
cnt=0
cnt1=0
for i in m:
    if len(i)%2==0:
        cnt+=1
    else:
        cnt1+=1
a=cnt*cnt1
print(a)