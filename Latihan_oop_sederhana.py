''' Algoritma : 1) Terdapat 2 hero beranama Sniper dan Rikimaru masing2 memiliki atribut Health, Power, Armor
                2) Sniper menyerang Rikimaru
                3) Rikimaru diserang Sniper
                4) Serangan power(AttackPower) Sniper dibagi armor Rikimaru sama dengan serangan diterima (AttackDiterima) / serangan terasa
                5) Total health dikurang serangan diterima (AttackDiterima) sama dengan sisa darah(health) Rikimaru
                7) Rikimaru menyerang Sniper
                8) Sniper diserang Rikimaru
                9) Serangan power(AttackPower) Rikimaru dibagi armor Sniper sama dengan serangan diterima (AttackDiterima) / serangan terasa
                10) Total health dikurang serangan diterima (AttackDiterima) sama dengan sisa darah(health) Sniper

'''
class Hero():
    def __init__(self, name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber


    def serang(self, lawan): # lawan = rikimaru, krn rikimaru adalah sebuah object(self), 'self', tipe data str, num dll merupakan object dari class didalam python
        print(f'{self.name} menyerang {lawan.name}')
        lawan.diserang(self) # agar rikimaru otomatis diserang tanpa dipanggil lagi menggunakan 'rikimaru.diserang()'

    def diserang(self, lawan):
        print(f'{self.name} diserang {lawan.name}')

h1_sniper = Hero('sniper', 100, 20, 10)
h2_rikimaru = Hero('rikimaru', 100, 50, 20)

h1_sniper.serang(h2_rikimaru)
# rikimaru.diserang() = otomatis dipanggil saat sniper menyerang