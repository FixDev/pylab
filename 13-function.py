def abs(bil):
    if bil < 0:
        return -bil
    else:
        return bil


# for i in range(-100, 0):
#     print(abs(i))


def diskriminan(a, b, c):
    return b * b - 4 * a * c


# diskriminan(10, 2, 4)


def getAverage(list_bilangan):
    count = len(list_bilangan)
    sum = 0

    if(count == 0):
        return 0

    for bilangan in list_bilangan:
        sum += bilangan

    return sum/count


def getAverageWithoutCount(list_bilangan):
    sum = 0

    if(len(list_bilangan) == 0):
        return 0

    for bilangan in list_bilangan:
        sum += bilangan

    return sum/len(list_bilangan)


avg = getAverage([1000, 2, 3, 17, 50])

print('Rata-rata nilai adalah', avg)
