class Kompyuter:
    def __init__(self, nomi, narxi, yili, protsessori, xotirasi):
        self.nomi = nomi
        self.narxi = narxi
        self.yili = yili
        self.protsessori = protsessori
        self.xotirasi = xotirasi
        self.soni = 1
        
    def get_info(self):
        full = f"nomi: {self.nomi} "
        full += f"yili: {self.yili} "
        full += f"soni: {self.soni}"
        return full
    
    def update_soni(self, qiymat):
        self.soni = self.soni + qiymat
    
obj1 = Kompyuter("hp", 4500000, "2022", "Ryzen 5", "256 GB SSD")
obj2 = Kompyuter("Asus", 5500000, "2023", "Ryzen 7", "512 GB M2 SSD")
