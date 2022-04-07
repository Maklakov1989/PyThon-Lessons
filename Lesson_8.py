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
# print(('*' * 25), 'Задание №2 к лекции № 8', ('*' * 25))
# class my_exeption(ZeroDivisionError):
#     def __init__(self, param):
#         self.param = param
#     try:
#         param = input('Введите число, которое мы будем делить на 0: ')
#         y = param / 0
#     except:
#         print("А делить на ноль нельзя!!")
# print(('*' * 25), 'Задание №3 к лекции № 8', ('*' * 25))
# class Str_exeption(Exception):
#     def __init__(self, list):
#         self.list = list
# inp_data = input("Введите любые значения (цифры, слова, буквы): ")
# inp_data = inp_data.split(' ')
# inp_data = list(inp_data)
# data = []
# try:
#     for el in inp_data:
#         if type(el) == int:
#             data.append(el)
#             raise Str_exeption("В списке есть слова")
# except
#
#
# print('Хотите продолжить? y/n')
#     a = input()
#     f = []
#     while a == 'y':
#         print('Введите числа через пробел: ')
#         d =(input())
#         d = d.split(' ')
#         d = list(d)
#         for i in d:
#             i = int(i)
#             f.append(i)
#         print('Список новых чисел - ', f)
#         for number in f:
#             total = total + number
#         print(f'Cумма всех введённых чисел - {total}')
#         print('Хотите продолжить y/n')
#         a = input()
#     if a == 'n':
#         print('Задание завершено! Спасибо!!')
print(('*' * 25), 'Задание №4 к лекции № 8', ('*' * 25))
class Warehouse:
    def __init__(self, units):
         self.units = units
class Equipment:
    def __init__(self, type):
         self.type = type
class printer(Equipment):
    def __init__(self, type):
        self.type = type
class scaner(Equipment):
    pass
class xerox(Equipment):
    pass
