def reverseList():
    listBuah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
    listBuahTerbalik = []

    for i in range(len(listBuah) - 1, -1, -1):
        listBuahTerbalik.append(listBuah[i])

    print('LIST BUAH          => ', listBuah)
    print('LIST BUAH TERBAIK  => ', listBuahTerbalik)


reverseList()
