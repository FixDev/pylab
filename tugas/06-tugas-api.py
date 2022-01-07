# Aplikasi untuk mencari jawaban TTS
import requests
from tabulate import tabulate


class TTS:
    # Data constant untuk total row per page
    rows = 10

    def __init__(self, question="", order="", page=1):
        # Init state yang diperlukan
        self.question = question
        self.order = order
        self.page = page
        self.response = []
        self.total = 0

    def findAnswers(self):
        # Check isi question tidak boleh steing kosong
        if self.question == "":
            print("Pertanyaan harus diisi!")
            return
        # Hit api untuk mencari data jawaban
        response = requests.get(
            f"https://kunci-tts-api.vercel.app/api/answers?question={self.question}"
        )

        # Ambil hanya response jawaban
        res = response.json()["answers"]

        # Ambil response total data
        self.total = response.json()["total"]

        # Define header untuk table
        headers = ["Jawaban", "Kisi-kisi", "Bintang"]

        # Perulangan untuk mengubah bentuk data
        # Sesuai dengan documentasi tabulate
        for i in range(len(res)):
            self.response.append([res[i]["word"], res[i]["clue"], res[i]["stars"]])

        # Hitung pagination (Page keberapa)
        indexStart = self.rows * (self.page - 1)

        # Slice response untuk mendapatkan data sesuai page
        # Yang diinginkan
        self.response = self.response[indexStart : indexStart + self.rows]

        # Sorted response [ascending/descending]
        self.response = sorted(
            self.response,
            reverse=False if self.order == "asc" or self.order == "" else True,
        )

        # Print response as a table
        print()
        print("Table Hasil Pencarian")
        print(
            tabulate(
                self.response,
                headers,
                tablefmt="github",
            )
        )

        # Print total data untuk indikator pagination
        print(f"Total data : {self.total}")


print("================================================")
print("SELAMAT DATANG DI APLIKASI PENCARIAN JAWABAN TTS")
print("================================================")
print()
# Minta pertanyaan untuk dicari
question = input("Masukan pertanyaan TTS yang ingin dicari jawabannya : ")

# Pilih type order
order = input("Urutkan data [asc/desc] (Default adalah asc) : ")

# Buat class object baru
tts = TTS(question, order)

# Panggil Method/Function untuk mencari data
tts.findAnswers()

# Check data jika lebih dari 10
if tts.total > 10:
    # Define variable perulangan
    repeat = "Y"

    # Perulangan untuk meminta pagination
    while repeat == "Y":
        # Minta no page untuk bisa melihat page berikutnya
        page = int(
            input(
                "Masukan no page jika ingin melihat data lainnya (Wajib memasukan angka) : "
            )
        )

        # Buat class object baru
        tts = TTS(question, order, page)

        # Panggil Method/Function untuk mencari data
        tts.findAnswers()

        # Meminta confirmasi untuk melihat data selanjutnya
        repeat = input("Ingin melihat data lain (Y/N) : ")

        if repeat == "Y":  # Kondisi jika ingin mengulangi
            continue
        else:  # Kondisi jika tidak ingin mengulangi/selesai menggunakan aplikasi
            repeat = "N"

# Akhir dari aplikasi (Ucapan terimakasi!)
print("TERIMAKASIH SUDAH MENGGUNAKAN APLIKASI INI:)")
