# 1 xonali sonlarni qo'shish bo'yicha mashq bajaruvchi o'yin dasturi
from random import randint

ball = 0
xato = 0
while True:
    a = randint(1, 10)
    b = randint(1, 10)
    print(f"{a} + {b} =",end=" ")
    n = int(input())
    if n == a+b:
        ball += 1
        continue
    else:
        xato += 1

    if xato == 3:
        print("Game over")
        break

print(f"sizning balingiz {ball}")


# Men o'ylagan sonni top o'yin dasturi
from random import randint

urinish = 0
a = randint(1, 10)
while True:
    urinish +=1
    print("Men o'ylagan son necha?", end=" ")
    n = int(input())
    if n != a:
        print("yo'q bu son emas")
    else:
        print(f"Ha bu son {n}")
        break

print(f"siz {urinish} ta urinishda topdingiz")