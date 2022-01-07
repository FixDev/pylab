import math


def diskriminan(a, b, c):
    diskri = (b * b) - (4 * a * c)
    print(f'diskriminan nya adalah {diskri}')
    return diskri


def hitungAkar(a, b, c):
    x1 = 0
    x2 = 0
    diskri = diskriminan(a, b, c)

    if(diskri < 0):
        print('tidak memiliki akar nyata')
    elif(diskri == 0):
        x1 = x2 = (b + math.sqrt(diskri)) / (2*a)

        print(f'hanya memiliki satu akar tunggal yaitu {x1}')
    else:
        x1 = (b + math.sqrt(diskri)) / (2*a)
        x2 = (b - math.sqrt(diskri)) / (2*a)

        print(f"Akar persamaan kuadrat nya adalah {x1} dan {x2}")


def mencariAkarPersamaanKuadrat():
    isRepeat = 'Y'
    while isRepeat == 'Y':
        a = int(input('Masukan angka pertama = '))
        if(a == 0):
            isRepeat = input(
                'Bilangan pertama tidak boleh bernilai 0, Ingin mengulangi (Y/T): ').upper()
            continue
        b = int(input('Masukan angka kedua   = '))
        c = int(input('Masukan angka ketiga  = '))

        hitungAkar(a, b, c)


mencariAkarPersamaanKuadrat()
