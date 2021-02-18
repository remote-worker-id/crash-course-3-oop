# 1) Penggunaan __init__
# 2) Perbedaan class dan instance

class Hero():
    jumlah = 0 # Contoh kita menambah "class variable"
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # Dibawah ini merupakan "Instance variable(atribut) yang hanya bisa digunakan pada object hero1 dkk
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1 # menambahkan 1 disetiap program berjalan (bisa untuk mengecek jumlah object berjalan)
        print(f'Membuat hero dengan nama : {inputName}') # cek jumlah by name

hero1 = Hero('Sniper', 100, 10, 0)
print(Hero.jumlah)
hero2 = Hero('Alucard', 1000, 100, 200)
print(Hero.jumlah)
hero3 = Hero('Roger', 2000, 200, 300)
print(Hero.jumlah)

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)