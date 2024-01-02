class Kompyuter:
    number = 0
    def __init__(self, nomi, narxi, yili, protsessori, xotirasi):
        self.nomi = nomi
        self.narxi = narxi
        self.yili = yili
        self.protsessori = protsessori
        self.xotirasi = xotirasi
        self.soni = 1
        Kompyuter.number += 1
        self.id = Kompyuter.number
        
    def get_info(self):
        full = f"nomi: {self.nomi} "
        full += f"yili: {self.yili} "
        full += f"soni: {self.soni}"
        return full
    
    def update_soni(self, qiymat):
        self.soni = self.soni + qiymat
    
    def __repr__(self):
        return self.nomi + " " + str(self.soni)


class Kompyuter_dukon:
    def __init__(self, nomi, manzili, telefoni):
        self.nomi = nomi
        self.manzili = manzili
        self.telefoni = telefoni
        self.kompyuterlar = []
    
    def __repr__(self):
        return self.kompyuterlar
    
    def add_kompyuter(self, komp):
        self.kompyuterlar.append(komp)
    
    def get_kompyuter(self):
        return self.kompyuterlar
    
    def remove_kompyuter(self,obj):
        if obj in self.kompyuterlar:
            self.kompyuterlar.remove(obj)
            
         
obj1 = Kompyuter("hp", 4500000, "2022", "Ryzen 5", "256 GB SSD")
obj2 = Kompyuter("Asus", 5500000, "2023", "Ryzen 7", "512 GB M2 SSD")

dukon1 = Kompyuter_dukon("Solih", "Toshkent", "+998916547898")
dukon1.add_kompyuter(obj1)
dukon1.add_kompyuter(obj2)
