s = str(input())
m = list(s)
cnt=0
for i in m:
    if i=="a" or i=="A" or i=="o" or i=="O" or i=="i" or i=="I" or i=="u" or i=="U" or i=="e" or i=="E":
        cnt+=1
        
print(cnt)
        