class Person:
    def __init__(self, nama, tgl_lahir):
        self.full_name = nama
        self.birth_date = tgl_lahir

    def print_desc(self):
        return f'halo nama saya {self.full_name} saya lahir {self.birth_date}'


person1 = Person('Muhammad Fikri', '31-12-2001')

print(person1.print_desc())
