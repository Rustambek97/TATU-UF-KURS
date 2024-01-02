#massiv bilan for ishlatilishi
b = [2,3,14,312,43,2]
for i in b:
    print(i)

#===================================

#massiv bilan if ishlatilishi
b = [2,3,14,312,43,2]
a = 14
if a in b:
    print("bor")
else:
    print("yo'q")
    
#===================================

#satrlar bilan for ishlatilishi
b = "Uzbekistan"
for i in b:
    print(i)

#===================================

#satrlar bilan if ishlatilishi
b = "Uzbekistan"
a = "e"
if a in b:
    print("bor")
else:
    print("yo'q")

#===================================    
    
#algo 148-masala
a = list(input().split())

#1-usul
for i in a:
    if i[0] == "A":
        print(i)

#2-usul
for i in range(len(a)):
    if a[i][0] == "A":
        print(a[i])