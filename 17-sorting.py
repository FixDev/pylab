# Bublesort
def bubleSort():
    angka = [9, 5, 1, 2, 4, 6, 8, 2]
    n = len(angka)
    print('ini n', n)
    for i in range(n):
        print('ini i', i)
        print('ini untuk perulangan j', n - i - 1)
        for j in range(n - i - 1):
            print('ini j', j)
            if angka[j] > angka[j + 1]:
                angka[j], angka[j + 1] = angka[j + 1], angka[j]
                # temp = angka[j]
                # angka[j] = angka[j+1]
                # angka[j+1] = temp
    print(angka)


# bubleSort()

# Insertion Sort


def insertionSort():
    angka = [9, 5, 1, 2, 4, 6, 8, 2]
    n = len(angka)
    for i in range(1, n):
        key_item = angka[i]

        j = i - 1

        while j >= 0 and angka[j] > key_item:
            print('masuk while')
            angka[j+1] = angka[j]

            j -= 1
        print('enggak masuk')
        angka[j+1] = key_item

    print(angka)


insertionSort()
