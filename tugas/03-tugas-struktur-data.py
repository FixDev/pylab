def pengecehakanNilaiSiswa():
    nilai_hasil_akhir_siswa = [
        {'nama': 'Reza', 'nilai': 70},
        {'nama': 'Ciut', 'nilai': 63},
        {'nama': 'Dian', 'nilai': 80},
        {'nama': 'Badu', 'nilai': 40}
    ]

    siswa_lulus = []

    for siswa in nilai_hasil_akhir_siswa:
        if siswa['nilai'] < 65:
            continue
        siswa_lulus.append(siswa['nama'])

    print('Siswa yang lulus : ', siswa_lulus)


pengecehakanNilaiSiswa()
print('=========================================================')


def reverseList():
    listBuah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
    listBuahTerbalik = []

    for i in range(len(listBuah) - 1, -1, -1):
        listBuahTerbalik.append(listBuah[i])

    print('LIST BUAH          => ', listBuah)
    print('LIST BUAH TERBAIK  => ', listBuahTerbalik)


reverseList()
print('=========================================================')


def listDuplicated():
    listBuah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
    listBuahDuplicate = []

    for i in listBuah:
        listBuahDuplicate.extend((i, i))

    print('Duplicate List', listBuahDuplicate)


listDuplicated()
print('=========================================================')


def printKonsonanString():
    hurufVokal = ['a', 'i', 'u', 'e', 'o']
    string = 'Nurul Fikri'
    strKonsonan = ''

    for i in string:
        if i in hurufVokal:
            continue

        strKonsonan += i.replace(" ", "")

    print(strKonsonan)


printKonsonanString()
