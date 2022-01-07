def fakto(n):
    hasil = 1
    if n > 2:
        for i in range(2, n+1):
            hasil *= i
        return hasil

    return 2


n = int(input('Masukan nilai n: '))

_fakto = fakto(n)
print(f'{n}! = {_fakto}')
