def listDuplicated():
    listBuah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
    listBuahDuplicate = []

    for i in listBuah:
        listBuahDuplicate.extend((i, i))

    print('Duplicate List', listBuahDuplicate)


listDuplicated()
