def fibonacci(n):
    if n < 1:
        return [n]

    listBeforeN = fibonacci(n-1)
    firstnum = listBeforeN[-2] if len(listBeforeN) > 2 else 0
    secnum = listBeforeN[-1] if len(listBeforeN) > 2 else 1

    return listBeforeN + [firstnum + secnum]


length = int(input('Masukan panjang: '))
print(fibonacci(length - 1))
