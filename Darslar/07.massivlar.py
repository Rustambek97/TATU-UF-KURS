#1.massiv qiymatlarini consoldan o'qish
m = list(map(int, input().split()))

#2.oxiriga element qo'shish
m.append(15) 

#3.biror indeksiga element qo'shish, 2 chi indeksiga 50 qiymatini kiritadi
m.insert(2, 50)

#4.indeksi bo'yicha sug'urib olish
b = m.pop(2) 

#5.indeksi bo'yicha o'chirish
del m[3] 

#6.massivni qiymati bo'yicha birinchi topgan elementni o'chiradi
m.remove(23)

#7.berilgan qiymatli elementni indeksini topadi
b = m.index(21) 

#8.kichikdan kattaga qarab tartiblaydi
m.sort() 
b = sorted(a) 
b = sorted(a, reverse=True) #teskari tartibda saralash

#9.eng kattasini aniqlash
maxx = max(m) 

#10.eng kichigini aniqlash
minn = min(m) 

#11.massiv yig'indisini aniqlash
yigindi = sum(m)

#12. massiv uzunligini aniqlash
uzunligi = len(m) 

#13.massivni 2-indeksidan 6-indeksigacha bo'lgan qiymatlarni olish
b = m[2:6]

#14.massivni 3-indeksidan oxirigacha qiymatlarni olish
b = m[3:]

#15.massivni boshidan 6-indeksigacha bo'lgan qiymatlarni olish
b = m[:6]

#16.massivni 3-indeksidan oxirgi qiymatigacha olish
b = m[3:-1]

#17.massivni qiymatlarini teskasi tartibda olish
b = m[::-1]

#18.massivdan nusxa olish
m2 = m[:]
m2 = m.copy()

#19.massivni teskarisiga almashtirish
m.reverse()