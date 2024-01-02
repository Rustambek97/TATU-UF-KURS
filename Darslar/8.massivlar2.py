# massivning [a, b] o'rindagi qiymatlarini
# massivning eng kichik elementiga bo'lib chiqish

n = int(input())
m = list(map(int, input().split()))

a, b = map(int, input().split())
minn = min(m)

for i in range(0, n):
    if i>=a-1 and i<=b-1:
        m[i] = m[i]/minn
print(*m) 

#=================================================================================================

# massivning [a, b] oraliqga tegishli qiymatlari
# massivning eng kichik elementiga bo'lib chiqish

n = int(input())
m = list(map(int, input().split()))

a, b = map(int, input().split())
minn = min(m)

for i in range(0, n):
    if m[i]>=a and m[i]<=b:
        m[i] = m[i]/minn
print(*m) 

# *m massivning faqat qiymatlarini olish uchun
# yani [,...,] qavs vergul belgilarsiz chiqarish