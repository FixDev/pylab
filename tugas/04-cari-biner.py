def cari_biner(target, arr):
    arr.sort()
    batas_atas = len(arr) - 1
    batas_tengah = 0
    batas_bawah = 0

    while batas_bawah <= batas_atas:

        batas_tengah = (batas_atas + batas_bawah) // 2

        if arr[batas_tengah] < target:
            batas_bawah = batas_tengah + 1

        elif arr[batas_tengah] > target:
            batas_atas = batas_tengah - 1

        else:
            return batas_tengah

    return -1


arr = [1, 4, 6, 13, 12, 66, 10, 100]
res = cari_biner(13, arr)

if res == -1:
    print("Tidak ditemukan di dalam list")
else:
    print("Ditemukan didalam list index", str(res))
    print("Ditemukan didalam list angka", arr[res])
