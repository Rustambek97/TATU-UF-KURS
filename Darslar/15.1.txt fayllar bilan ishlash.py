class Text:
    def __init__(self, name):
        self.name = name + ".txt"
        with open(f"{self.name}","x") as file:
            pass
    
    def uqish(self):
        with open(self.name, 'r') as file:
            matn = file.read()
        return matn
    
    def yozish(self, matn):
        with open(self.name, 'w') as file:
            file.write(matn)
    
    def qushish(self, matn):
        with open(self.name, 'a') as file:
            file.write(matn)
    
    def massiv(self):
        with open(self.name, 'r') as file:
            massiv = file.readlines()
            massiv = [i.rstrip() for i in massiv]
        return massiv
    
    def bir_qator(self):
        matn = self.uqish()
        matn = matn.rstrip()
        matn = matn.replace('\n', '')
        self.yozish(matn)
        return matn

myfile = Text("myfayl")
myfile.qushish("Mana senga \nolam olam guuul \netagingga siqqaningchaa ooool \n")
print(myfile.uqish())
print(myfile.massiv())
print(myfile.bir_qator())
            
            
            
            
