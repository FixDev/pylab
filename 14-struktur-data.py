def bilanganList():
    bilangan = [1, 2, 3]

    a = bilangan.pop()

    bilangan.append(5)

    print(f"Bilangan {bilangan}")

    print(f"Bilangan {a}")


def bilanganQueue():
    bilangan = [1, 2, 3]

    a = bilangan.pop(0)

    bilangan.append(4)

    print(f"Bilangan {bilangan}")

    print(f"Bilangan {a}")


def insertListSpesifik():
    bilangan = [1, 2, 3]

    a = bilangan.pop(2)

    bilangan.insert(0, 'hehe')

    print(f"Bilangan {bilangan}")

    print(f"Bilangan {a}")


def setHimpunan(type='add'):
    a = {6, 5, 4}
    if(type == 'add'):
        a.add(3)
    elif(type == 'remove'):
        a.remove(5)
    else:
        a.pop()

    print(f"Himpunan {a}")


def setUnionUpdateHimpunan(type='union'):
    set1 = {1, 2, 3}
    set2 = {2, 4, 6}

    if(type == 'union'):
        set3 = set1.union(set2)
        print(set3)
    else:
        set1.update(set2)
        print(set1)


def dictionary():
    data_diri = {
        "nama": "Muhammad Fikri",
        "matkul": "DDP"
    }

    data_diri["nama"] = 1

    print(data_diri["nama"])
    print(data_diri["alamat"])


bilanganList()
bilanganQueue()
insertListSpesifik()
setHimpunan()
setUnionUpdateHimpunan()
dictionary()
