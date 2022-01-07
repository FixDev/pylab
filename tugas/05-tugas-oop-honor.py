class Pegawai:
    honor_per_jam = 30000

    def __init__(self, nama, total_jam_kerja):
        self.nama = nama
        self.total_jam_kerja = total_jam_kerja

    def honor(self):
        return f"Pegawai dengan nama {self.nama}, memiliki honor sebesar {self.total_jam_kerja * self.honor_per_jam}"


pegawai1 = Pegawai('Muhammad Fikri', 8)

print(pegawai1.honor())
