# text fayllar bilan ishlash uchun class
class Text:
    def __init__(self, nomi):
        self.nomi = nomi
        with open(f"{self.nomi}", "w") as fayl:
            pass
    
    def uqish(self):
        with open(f"{self.nomi}", "r") as fayl:
            return fayl.read()
    
    def yozish(self, matn):
        with open(f"{self.nomi}", "w") as fayl:
            fayl.write(matn)
    
    def frist_row(self):
        with open(f"{self.nomi}", "r") as fayl:
            return fayl.readline()
        
    def massiv(self):
        with open(f"{self.nomi}", "r") as fayl:
            lines = fayl.readlines()
            lines = [i.strip() for i in lines]
            return lines
        
    def del_abzas(self):
        with open(f"{self.nomi}" , "r") as fayl :
            d = fayl.readlines()
            s = ""
            for i in d:
               s += i.rstrip() 
            self.yozish(s)
            return s
    
    def __repr__(self):
        with open(f"{self.nomi}" , "r") as fayl :
            d = fayl.read()
            s = len(d)
            return str(s) 
    
    def __getitem__(self , n):
        with open(f"{self.nomi}" , "r") as fayl :
            return fayl.readlines()[n-1]
    
    def del_row(self , n): #x
        with open(f"{self.nomi}" , "r") as fayl :
            lines = fayl.readlines()
            lines = [i.strip() for i in lines]
            s = lines[::n] + lines[n+1::]
            return s
    
    def del_rows(self , n  ,m): #x
        with open(f"{self.nomi}" , "r") as fayl :
            lines = fayl.readlines()
            lines = [i.strip() for i in lines]
            s = lines[:n] + lines[m:]
            return s
        
    def get_row(self,n):
        with open(f"{self.nomi}" , "r") as fayl:
            d = fayl.readlines()
            d = [i.strip() for i in d]
            s = d[n-1]
            return s
        
    def upper_row(self):
        S = self.uqish()
        S_massiv = S.split("\n")
        natija = []
        for qator in S_massiv:
            a = qator.split(" ")
            t = ""
            for i in a:
                t += i.title()+" "
            natija.append(t+"\n")
        a = ""
        for qator in natija:
            a += qator
        self.yozish(a)