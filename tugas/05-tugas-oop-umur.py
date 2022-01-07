import datetime


class Person:
    def __init__(self, nama, tgl_lahir):
        date = tgl_lahir.split('-')
        _date = list(map(int, date))
        _date.reverse()
        self.full_name = nama
        self.birth_date = datetime.datetime(_date[0], _date[1], _date[2])
        self.age = datetime.datetime.now().year - self.birth_date.year

    def print_desc(self):
        return f'halo nama saya {self.full_name}, saya lahir {self.birth_date.date()}, dan saya berumur {self.age}'

    def umur(self):
        return f'saya berumur {self.age}'


person1 = Person('Muhammad Fikri', '31-12-2001')

print(person1.print_desc())
print(person1.umur())
