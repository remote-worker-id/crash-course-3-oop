from geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, alas, tinggi):
        self.a = alas
        self.t = tinggi


    def info(self):
        return f'ini adalah object dari segitiga dengan alas = {self.a} dan tinggi = {self.t}'


    def hitung_luas(self):
        return self.a * self.t / 2
