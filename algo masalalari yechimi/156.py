s = str(input())

i,j = map(int,input().split(" "))

l = list(s.split(" "))

empty = l[i-1]
l[i-1] = l[j-1]
l[j-1] = empty

S = ""

for i in l:
    S += i + " "

print(S[:-1])