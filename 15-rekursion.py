def jumlah(n):
    if(n == 0):
        return 0
    return n + jumlah(n-1)


print(jumlah(2))


def fibo(n):
    if (n < 1):
        return 0
    if (n == 1):
        return 1
    if(n == 2):
        return 1
    return fibo(n-1) + fibo(n-2)


for i in range(1, 10):
    print(fibo(i))
