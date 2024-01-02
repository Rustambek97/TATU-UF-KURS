n = int(input())
m = list(map(int, input().split()))

middle = sum(m)/len(m)

S = [x for x in m if x < middle]

b = sum(S)/len(S)

print("%.2f"%b)



