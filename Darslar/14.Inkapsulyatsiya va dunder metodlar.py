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
        self.__id = Kompyuter.number
    
    def get_id(self):
        return self.__id
    
    def change_id(self, new_id):
        self.__id = new_id
    
    @classmethod
    def kompyuterlar_soni(cls):
        return cls.number
    
    def get_info(self):
        full = f"nomi: {self.nomi} "
        full += f"yili: {self.yili} "
        full += f"soni: {self.soni}"
        return full
    
    def update_soni(self, qiymat):
        self.soni = self.soni + qiymat
    
    def __repr__(self):
        return self.nomi + " " + str(self.soni)
    
    def __call__(self, p):
        return self.nomi + p
    
obj1 = Kompyuter("hp", 4500000, "2022", "Ryzen 5", "256 GB SSD")
obj2 = Kompyuter("Asus", 5500000, "2023", "Ryzen 7", "512 GB M2 SSD")
obj3 = Kompyuter("Acer", 6500000, "2023", "Ryzen 7", "512 GB M2 SSD")


class Kompyuter_dukon:
    def __init__(self, nomi, manzili, telefoni):
        self.nomi = nomi
        self.manzili = manzili
        self.telefoni = telefoni
        self.kompyuterlar = []
    
    def get_info(self):
        return f"{self.nomi} {self.manzili}"
    
    def __repr__(self):
        return self.nomi
    
    # def __str__(self): # repr bilan bir xil vazifani bajaradi
    #     return self.nomi
    
    def __getitem__(self, index):
        if index==0:
            return self.nomi
        elif index==1:
            return self.manzili
        elif index==2:
            return self.telefoni
    
    def __setitem__(self, index, qiymat):
        if index==0:
            self.nomi=qiymat
        elif index==1:
            self.manzili=qiymat
        elif index==2:
            self.telefoni=qiymat
    
    def __call__(self, komp):
        self.kompyuterlar.append(komp)
    
    def get_kompyuter(self):
        return self.kompyuterlar
dukon1 = Kompyuter_dukon("Solih", "Toshkent", "+998916547898")

