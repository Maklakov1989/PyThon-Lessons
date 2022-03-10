# print(('*' * 25), 'Задание №1', ('*' * 25))
#
# def devide(number_1, number_2):
#     try:
#         return number_1 / number_2
#     except: ZeroDivisionError
# number_1 = int(input('Введите 1 число: '))
# number_2 = int(input('Введите 2 число: '))
# print(devide(number_1, number_2))
# print(('*' * 25), 'Задание №2', ('*' * 25))
# def person():
#     return print(name,surname, date_of_birth, city, e_mail, tel)
# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# date_of_birth = input('Введите дату рождения: ')
# city = input('Введите место рождения: ')
# e_mail = input('Введите e-mail: ')
# tel = input('Введите телефон: ')
# person()
# print(('*' * 25), 'Задание №3', ('*' * 25))
# def max_func():
#     s = max(x)
#     x.remove(s)
#     s2 = max(x)
#     return [s, s2]
# a = int(input('Введите занение 1: '))
# b = int(input('Введите занение 2: '))
# c = int(input('Введите занение 3: '))
# x = [a, b, c]
# print(max_func())
print(('*' * 25), 'Задание №4', ('*' * 25))
x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
"""Возведение в степень встроенной командой"""
def my_func_1 (x, y):
        return x**y
print(my_func_1(x, y))
"""Возведение в степень без встроенной команды"""
def my_func_2 (x, y):

    return x**y
print(my_func_1(x, y))