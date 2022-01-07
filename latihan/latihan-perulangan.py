# Latihan 1
def latihan1():
    rows = int(input('Masukan jumlah baris yang diinginkan : '))
    for i in range(1, rows+1):
        for _ in range(i):
            print(" ", end=" ")
        for _ in range(rows - i + 1):
            print("*", end=" ")
        print()


# Latihan 2
def latihan2():
    rows = int(input('Masukan jumlah baris yang diinginkan : '))
    for i in range(rows, 0, -1):
        for _ in range(rows-i):
            print(end=" ")
        for _ in range(2*i):
            print('*', end='')
        print()


# Latihan 3
def latihan3():
    rows = int(input('Masukan jumlah baris yang diinginkan : '))
    for i in range(rows, 0, -1):
        for _ in range(rows-i):
            print(end=" "*3)
        for _ in range(2*i):
            print('*', end=' '*2)
        print()


# Latihan 4
def latihan4():
    rows = 9
    for i in range(1, rows+1):
        if(i == 1 or i == 9):
            for _ in range(1, 21):
                print("-", end=" ")
        else:
            for j in range(1, 21):
                if(j == 1 or j == 20):
                    print("|", end=" ")
                elif(i == 3):
                    print('-', end=" ")
                else:
                    print(end=" "*2)
        print()


# Latihan 5
def latihan5():
    row = 2
    length = 30
    for i in range(1, row+1):
        if(i % 2 == 1):
            for j in range(1, length+1):
                if(j == 10):
                    print(1, end="")
                elif(j == 20):
                    print(2, end="")
                elif(j == 30):
                    print(3, end="")
                else:
                    print(end=" ")
            print()
        else:
            for _ in range(1, 4):
                print('123456789', end="")
                print('0', end="")
    print()


print("Latihan 1")
print("------------------------------")
latihan1()
print("------------------------------")
print("Latihan 2")
print("------------------------------")
latihan2()
print("Latihan 3")
print("------------------------------")
latihan3()
print("------------------------------")
print("Latihan 4")
print("------------------------------")
latihan4()
print("------------------------------")
print("Latihan 5")
print("------------------------------")
latihan5()
print("------------------------------")
