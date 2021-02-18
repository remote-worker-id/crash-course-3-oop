# Method tanpa return dan tanpa argument (void function), method dengan argument tanpa return, method dgn reteurn
# Method sama seperti function
class Hero():
    # class variable
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Instance Variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    # 1) void function, method tanpa return dan argument
    def siapa(self):
        print(f'Nama hero adalah : {self.name}')

    # 2) Method dengan argument, tanpa return (bisa menambah nilai argument object)
    def HealthUp(self, up):
        self.health += up

    # 3) Methode denga return
    def getHealth(self):
        return self.health

hero1 = Hero('Sniper', 100, 100, 50)
hero2 = Hero('Alucard', 200, 150, 30)
hero3 = Hero('Gatot', 2000, 1500, 300)

# Panggil 1
hero1.siapa()

# Panggil 2 (tambah health 100, output di panggil 3)
hero1.HealthUp(100)

# Panggil 3
print(f'Health hero saat ini : {hero1.getHealth()}')

