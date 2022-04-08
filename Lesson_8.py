print(('*' * 25), 'Задание №1 к лекции № 8', ('*' * 25))
class Date:
    @classmethod
    def get_day(cls, param):
        x = param.split('-')
        my_dict = {'первое' : "01", 'второе' : "02", 'третье' : "03", 'четвёртое' : "04", 'пятое' : "05",
                   'шестое' : "06", 'седьмое' : "07", 'восьмое' : "08", 'девятое' : "09", 'десятое' : "10"}
        day = my_dict[x[0]]
        print(f'Введённое пользователем число - {day}')
    @staticmethod
    def get_month(param):
        x = param.split('-')
        my_dict_2 = {'января': "01", 'февраля': "02", 'марта': "03", 'апреля': "04", 'мая': "05",
                   'июня': "06", 'июля': "07", 'августа': "08", 'сентября': "09", 'октября': "10",
                   'ноября': "11", 'декабря': "12"}
        month = my_dict_2[x[1]]
        print(f'Введённый пользователем месяц - {month}')
Date.get_day("десятое-декабря-2010")
Date.get_month("десятое-декабря-2010")
print(('*' * 25), 'Задание №2 к лекции № 8', ('*' * 25))
class my_exeption(ZeroDivisionError):
    def __init__(self, param):
        self.param = param
    try:
        param = input('Введите число, которое мы будем делить на 0: ')
        y = param / 0
    except:
        print("А делить на ноль нельзя!!")
print(('*' * 25), 'Задание №3 к лекции № 8', ('*' * 25))
class Str_exeption(Exception):
    def __init__(self, list):
        self.list = list
inp_data = input("Введите любые значения: ")
inp_data = inp_data.split(' ')
res = []
for item in inp_data:
    try:
        res.append(int(item))
    except ValueError:
        pass
print('Введены числа - ', res)
print('Хотите продолжить? y/n')
a = input()
f = []
while a == 'y':
    add_data = input('Введите любые значения через пробел: ')
    add_data = add_data.split(' ')
    for item in add_data:
        try:
            res.append(int(item))
        except ValueError:
            pass
    print('Список новых чисел - ', res)
    print('Хотите продолжить y/n')
    a = input()
    if a == 'n':
        print('Задание завершено! Спасибо!!')
#
# print(('*' * 25), 'Задание №4 к лекции № 8', ('*' * 25))
# class Warehouse:
#     def __init__(self, quonts):
#          self.quonts = quonts
# class Equipment:
#     def __init__(self, units, type):
#         self.units = units
#         self.type = type
#         to_wh = {}
# class printer(Equipment):
#     def __init__(self, type, quont):
#         self.type = type
#         self.quont = quont
#         to_wh[self.type] = self.quont
# class scaner(Equipment):
#     def __init__(self, type):
#         self.type = type
# class xerox(Equipment):
#     def __init__(self, type):
#         self.type = type