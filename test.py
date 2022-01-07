master_produk = {
    "SM1": {
        "namaproduk": 'SHAMPOO 1',
        "harga": 12000
    },
    "SM2": {
        "namaproduk": 'SHAMPOO 2',
        "harga": 15000
    },
}

kode_produk = input("Masukan kode produk   : ").upper()
jumlah_produk = int(input("Masukan jumlah produk : "))

produk_dipilih = master_produk[kode_produk]
harga = produk_dipilih['harga'] * jumlah_produk

if(harga > 250000):
    _harga = harga
    harga -= (5 * _harga) / 100
    harga += (10 * _harga) / 100

print()
print("STRUK PEMBELIAN")
print("==========================")
print("KODE PRODUK      :", kode_produk)
print("KODE NAMA PRODUK :", master_produk[kode_produk]['namaproduk'])
print("JUMLAH ITEM      :", jumlah_produk)
print("TOTAL HARGA      :", harga)
print("==========================")
