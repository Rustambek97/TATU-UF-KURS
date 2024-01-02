# a va b sonlari kiritilganda kattasini aniqlash dasturi
a = int(input())
b = int(input())

# 1) avval if qismidagi shart tekshiriladi, to'g'ri bo'lsa ishlaydi va
# keyingi qismlar tekshirilmaydi
# 2) so'ng elif lar tekshiriladi, elif bir nechta bo'lishi mumkin
# qaysi to'g'ri bo'lsa ishlaydi va keyingilari tekshirilmaydi
# 3) oxirda else tekshiriladi, hech bir shart bajarilmasa ishlaydi

if a>b:
    print("a soni katta")
elif a==b:
    print("a va b teng")
else:
    print("b katta")

# Quyidagicha yozilsa barchasi ketma ket tekshiriladi

if a>b:
    print("a soni katta")
if a==b:
    print("a va b teng")
if a<b:
    print("b katta")