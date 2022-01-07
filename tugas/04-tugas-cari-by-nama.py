def find_name(name, listName):
    if name in listName:
        return 'Nama ' + name + ' telah ditemukan'

    return 'Nama tidak ditemukan dalam list'


listName = ['Abdul', 'Fikri', 'Hamzah', 'Ira', 'Kosasih']
print(find_name('Fikri', listName))
