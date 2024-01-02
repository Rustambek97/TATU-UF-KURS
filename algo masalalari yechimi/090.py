from math import log, e, sin, pow, atan, pi
a,b,c = map(int,input().split(" "))
S=0
i=-pi
h=pi/10
while i<=pi:
    S+=(log(pow(a,2*sin(i)),e)+pow(e,2*i))/(atan(i)+b)+c
    i+=h
print((f"{S:.2f}"))