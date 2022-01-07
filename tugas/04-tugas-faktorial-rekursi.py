def faktorial(n):
    if n > 2:
        return n * faktorial(n - 1)

    return 2


n = int(input('Masukan nilai n: '))

_faktorial = faktorial(n)
print(f'{n}! = {_faktorial}')
