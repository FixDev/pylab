def contoh_pertama():
    row = int(input('Masukan jumlah baris yang diinginkan : '))  # row = 5
    # i = 2
    for i in range(row):  # antara number dari parameter 1 sampai parameter 2
        for _ in range(i+1):  # loop ke 2 untuk kolom
            print('* ', end=" ")  # print kolom sesui dengan baris
        print()


def contoh_kedua():
    row = int(input('Masukan jumlah baris yang diinginkan : '))
    star = ''

    for i in range(0, row):
        for _ in range(0, i+1):
            star += '* '
        star += '\n'
    print(star, end=' ')


contoh_pertama()
