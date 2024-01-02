s = str(input())

i = int(input())

l = list(s.split(" "))

empty = l[i-1]
l[i-1] = "TATU"

S = ""

for i in l:
    S += i + " "

print(S[:-1])