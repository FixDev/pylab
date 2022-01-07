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
