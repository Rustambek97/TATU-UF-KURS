import math
a1,a2,a3 = map(int,input().split(" "))


s1=math.pow(a1,2)*math.pi
s2=math.pow(a2,2)*math.pi
s3=math.pow(a3,2)*math.pi

print(f"{s1:.2f}" , end=(" "))
print(f"{s2:.2f}" , end=(" "))
print(f"{s3:.2f}")
