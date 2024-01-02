# satrli o`zgaruvchilarga qiymat berish
a = 'bittalik qo`shtirnoq'
a2 = "ikkitalik qo`shtirnoq"
a3 = """3 ta ikkitalik 
qo`shtirnoq, bunda qiymatni
ko`p qatorli qilib 
kiritish ham mumkin"""

# consoldan o`qish
b1 = input()
b2 = str(input())

# satrni har bir so'zini list qilib o'qish
c1 = list(input().split())

# satrni har bir abzastini list qilib o'qish
c2 = list(a.split("\n"))

# a satr uzunligini aniqlash
l = len(a) 

# a satrni katta harflarga o'tkazish
b1 = a.upper()

# a satrni kichik harflarga o'tkazish
b2 = a.lower()

# har bir so'zni bosh harfini kattaga o'tkazish
b3 = a.title()

# a satrdan bitta belgini olish
b1 = a[3] 

# a satrdan [1,4) oraliq indeksidagi belgilarini qirqib olish
b2 = a[1:4]

# a satrdan [0,8) oraliq indeksidagi belgilarini qirqib olish
b3 = a[:8]

# a satrdan 3-indeksdan oxirigacha qirqib olish
b4 = a[3:]

# a satrdan [0,-3) oraliq ya'ni oxiridan 3 oldingi belgisigacha qirqib olish
b5 = a[:-3]

# a satrni teskari tartibda ifodalash
b6 = a[::-1]

# a satrdan 5 marta takroran yozish
b7 = a*5

# a satrdagi tan yozuvi qatnashganlarni tojikiston yozuviga almashtirish
b8 = a.replace("tan","tojikiston")

# ASCII kodlash jadvalidan belgining kodini olish
c1 = ord("A")    # javobi 65

# ASCII kodlash jadvalidan kodning belgisini olish
c2 = chr(65)     # javobi A