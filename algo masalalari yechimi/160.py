s = str(input())

S = ""
for i in s:
    if i == i.upper():
        i = i.lower()
    elif i == i.lower():
        i = i.upper()
    S += i
    

print(S)