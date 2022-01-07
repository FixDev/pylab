def penggajianKaryawan():
    # Constant variable
    gapok = 15000000
    tukel = 0
    tunak = 0
    totalGaji = 0
    isRepeat = 'Y'

    while isRepeat == 'Y':
        # Define variable
        nama = input('Masukkanan nama: ')
        sudahMenikah = input('Apakah sudah menikah (Y/T): ').upper()
        jumlahAnak = 0
        if(sudahMenikah == 'Y'):
            jumlahAnak = int(input('Masukkan jumlah anak: '))
        punyaAnak = jumlahAnak > 0

        # Logic
        if(sudahMenikah == 'Y'):
            tukel += (20 * gapok) / 100

            if(punyaAnak and jumlahAnak < 2):
                tunak = ((jumlahAnak * 10) * gapok) / 100
            else:
                tunak = (20 * gapok) / 100

        totalGaji = gapok + tukel + tunak

        # Output
        print('Detail Gaji', nama)
        print('Gaji Pokok         : ', int(gapok))
        print('Tunjangan Keluarga : ', int(tukel))
        print('Tunjangan Anak     : ', int(tunak))
        print('Jumlah Total       : ', int(totalGaji))

        # Ask For Repeat
        isRepeat = input('Ingin mengulangi (Y/T): ').upper()


def showDataPegawai():
    daftar_pegawai = [{"nama": "Budi", "gaji": 1500000},
                      {"nama": "Cici", "gaji": 2000000}]

    print('| Nama | Gaji    |')
    for i in daftar_pegawai:
        print('|', i['nama'], '|', i['gaji'], "|")


def printBintang():
    row = 7
    for i in range(0, row):
        for _ in range(1, row-i):
            print('.', end=' ')
        for _ in range(2*i):
            print('*', end=' ')
        for l in range(i - 1, row-2):
            print(".", end=' ')
        print()


def printBintangDua():
    rows = 7
    for i in range(0, rows):
        for j in range(rows - 1, i, -1):
            print(".", "", end='')
        for k in range(i):
            print("* " * 2, end='')
        for l in range(i + 1, rows):
            print(".", '', end='')
        print()


# printBintangDua()
# printBintang()

# showDataPegawai()

penggajianKaryawan()
# print('Terimakasih.')
