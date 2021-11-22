class Menu: 
    def __init__(self, nama, harga = 0):
        self.nama = nama
        self.harga = harga
        if self.nama == "ayam bakar" or self.nama == "Ayam Bakar":
            self.harga = 25000
        elif self.nama == "ayam kecap" or self.nama == "Ayam Kecap":
            self.harga = 15000
        elif self.nama == "mie ayam" or self.nama == "Mie Ayam":
            self.harga = 15000
        elif self.nama == "sate ayam" or self.nama == "Sate Ayam":
            self.harga = 25000
        elif self.nama == "sate kambing" or self.nama == "Sate Kambing":
            self.harga = 30000
    def jumlahHarga(self, jumlah):
        self.harga *= jumlah
        return self.harga
