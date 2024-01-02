a,b,c = map(int,input().split(" "))
S=0
for i in range(1,11,3):
    S+=a*(i**2)/b+i/c
print(f"{S:.2f}")