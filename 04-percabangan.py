# Program Pengechekan Umur IF ELSE
def checkBolehNontonFilm():
    umur = int(input('Masukkan Umur : '))

    print("Umur anda %d" % umur)

    if(umur < 17):
        print('Anda belum boleh nonton film ini')
    else:
        print('Anda boleh menonton film ini')

    print('Terimakasih')


# Program Pengecheckan Grade Nilai
def checkGradeNilai():
    nilai = int(input('Masukan nilai anda : '))
    grade = ''
    if(nilai < 60):
        grade = 'E'
    elif(nilai < 70):
        grade = 'D'
    elif(nilai < 80):
        grade = 'C'
    elif(nilai < 90):
        grade = 'B'
    else:
        grade = 'A'

    print("Grade anda adalah %s" % grade)


# Program Check True Number
def checkIsNumber(number):
    if(number < 200):
        if(number == 150):
            print('number is %d' % number)
        elif(number == 100):
            print('number is %d' % number)
        elif(number == 50):
            print('number is %d' % number)
        elif(number < 50):
            print('value less then 50')
    else:
        print('not find true condition')

    print('Good bye')


checkIsNumber(50)
