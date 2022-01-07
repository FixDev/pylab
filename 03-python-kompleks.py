def tampilkanStatusTugas(nama, nilai):
    status = ''

    if nilai > 70:
        status = "Lulus"
    else:
        status = 'Ulangi'

    print('Siswa yang bernama %s meiliki nilai sebesar %d berstatus %s' %
          (nama, nilai, status))


tampilkanStatusTugas('Muhammad Fikri', 80)
