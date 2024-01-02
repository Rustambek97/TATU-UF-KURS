class Shaxs:
    number = 0
    def __init__(self, ism, familiya, t_sanasi):
        self.ism = ism
        self.familiya = familiya
        self.t_sanasi = t_sanasi
        Shaxs.number += 1
        self.id = Shaxs.number
    
    def get_info(self):
        return f"{self.ism} {self.familiya} {self.t_sanasi}"
    
    def set_t_sanasi(self,new_sana):
        self.t_sanasi = new_sana
    
    def __repr__(self):
        return self.ism
        
a = Shaxs("Alisher", "Botirov", "2001-10-15")

class Xodim(Shaxs):
    def __init__(self, ism, familiya, t_sanasi, ish_staji, oyligi):
        super().__init__(ism, familiya, t_sanasi)
        self.ish_staji = ish_staji
        self.oyligi = oyligi
    
    def get_info(self):
        full = super().get_info()
        full += f"{self.ish_staji} {self.oyligi}"
        return full
    

b = Xodim("Sanjar", "To'rayev", "2002-08-21", "5 yil", 800000)




        
        
        
        
