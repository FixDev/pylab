n = 5
star = ''

for i in range(1, n+1):
    for j in range(i, 0, -1):
        star += ' '
    star += '* \n'

print(star)
