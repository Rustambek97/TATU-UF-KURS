from math import pow, cos
x,y,c,d = map(int, input().split(" "))
S = 0
P = 1
SP = 0
sp = 0
for a in range(1,x+1):
    S+= pow(2*a+cos(a),2)

for a in range(1,y+1):
    P *= (a+6)/pow((pow(a,2)+2),1/2)

for k in range(1,c+1):
    for y in range(1,d+1):
        sp += (pow(k,2)+y)/pow(pow(k,2)+pow(y,2),1/2)
    SP += sp
    sp = 0

print(f"{S:.2f} {P:.2f} {SP:.2f}")
