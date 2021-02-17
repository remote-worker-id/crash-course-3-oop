from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        # Fungsi yang dipanggil pertama kali saat opbject diciptakan
        self.p = p
        self.l = l


    def info(self):
        return f'ini adalah object dari persegipanjang dengan panjang = {self.p} dan lebar = {self.l}'


    def hitung_luas(self):
        return self.p * self.l
