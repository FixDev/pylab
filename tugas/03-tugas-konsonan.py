def printKonsonanString():
    hurufVokal = ['a', 'i', 'u', 'e', 'o']
    string = 'Nurul Fikri'
    strKonsonan = ''

    for i in string:
        if i in hurufVokal:
            continue

        strKonsonan += i.replace(" ", "")

    print(strKonsonan)


printKonsonanString()
