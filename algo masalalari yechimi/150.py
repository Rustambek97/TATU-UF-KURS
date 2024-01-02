s = str(input())
m = list(s.split(" "))

for i in m:
    for j in range(0,len(i)-3):
        if i[j:j+4].lower()=="info":
             print(i , end=" ")
             break