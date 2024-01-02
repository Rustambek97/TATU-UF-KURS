n = int(input())
s = map(str,input().split(" "))
m = list(s)
cnt=0

for i in m:
    if i == "A":
       m.remove("A") 
       cnt+=1
    if i == "S":
        m.remove("S") 
        cnt+=1
    if i == "A":
       m.remove("S") 
       cnt+=1
    if i == "A":
       m.remove("A") 
       cnt+=1
    if i == "L":
       m.remove("L") 
       cnt+=1
    if i == "O":
       m.remove("O") 
       cnt+=1
    if i == "M":
       m.remove("M") 
       cnt+=1
       
if cnt==7:
    print("YES")
else:
    print("NO")
       
       
       
       
       