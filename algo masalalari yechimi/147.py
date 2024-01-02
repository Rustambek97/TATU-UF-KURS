s = str(input())
S = s.upper()


cnt=0
cnt2=0
for i in S:
    if i=="A":
        cnt+=1
    if i=="Y":
        cnt2+=1
print(cnt)
print(cnt2)
