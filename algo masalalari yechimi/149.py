s = str(input())
m = list(s.split(" "))
cnt=0
s=""
for i in m:
    if i[-2:] =="NA":
        cnt+=1
        s += i +" "
print(cnt)
print(s[:-1])

        
        