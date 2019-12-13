from datetime import date

def my_func():
    print("Это моя функция")

def deco(f):
    def wrap(f):
        print("Что-то перед выполнением")
        f()
        print("Что-то после выполнением")


result = deco(my_func)
# print(result())
class Person:
    def __init__(self, data=list()) :
        self.data = data

    def get_data(self):
        return self.data[0:3]

    def set_data(self, data):
        self.data = data

#
#     @staticmethod
#     def is_adult(age):
#         return age > 18
#
#     @classmethod
#     def from_birth_day(cls, name, year):
#         return cls(name, date.today().year - year)
#
# # p2 = Person.from_birth_day('BACR', 1991)
# # print(p2.age)
# # # p = Person("BACR")
# # # p.age = 25
# # # print(Person.is_adult(p.age))