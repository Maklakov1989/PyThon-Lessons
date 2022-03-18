# print(('*' * 25), 'Задание №1', ('*' * 25))
#
# def devide(number_1, number_2):
#     try:
#         return number_1 / number_2
#     except: ZeroDivisionError
# number_1 = int(input('Введите 1 число: '))
# number_2 = int(input('Введите 2 число: '))
# print(f'Число 1 делить на число 2 равно - {devide(number_1, number_2)}')
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
#     print(s, s2)
#     return s + s2
# a = int(input('Введите занение 1: '))
# b = int(input('Введите занение 2: '))
# c = int(input('Введите занение 3: '))
# x = [a, b, c]
# print(f'Сумма максимальных 2-х значений из введённых - {max_func()}')
# print(('*' * 25), 'Задание №4', ('*' * 25))
# x = int(input('Введите действительное положительное число: '))
# y = int(input('Введите целое отрицательное число: '))
# """Возведение в степень встроенной командой"""
# def my_func_1 (x, y):
#         return x**y
# print(f'Результат функции 1: {my_func_1(x, y)}')
# """Возведение в степень без встроенной команды"""
# i = 1
# def my_func_2 (x, y):
#     for i in range(abs(x)):
#         i = y
#         i = 1/(x * x)
#         return i
# print(f'Результат функции 2: {my_func_2(x, y)}')

print(('*' * 25), 'Задание №5', ('*' * 25))
# numbers = None
# def numbers_summ():
#     numbers = input('Введите числа, разделённые пробелом: ')
#     numbers = numbers.split(' ')
#     numbers = list(numbers)
#     spisok = []
#     for i in numbers:
#         i = int(i)
#         spisok.append(i)
#     print(spisok)
#     total = 0
#     for number in spisok:
#         total = total + number
#     return total
# print(numbers_summ())
# number_add = 0
# for number_2 in number_add:
#     number_2 = input('Добавьте числа')
#     if number_2 == 'нет':
#         break
#     else:
#         number_2 = number_2.split(' ')
#         number_2 = list(number_2)
#         spisok2 = []
#         for i in numbers:
#             i = int(i)
#             spisok2.append(i)
#         print(spisok2)
#         total2 = 0
#         for number in spisok2:
#             total2 = numbers_summ() + number
#         print(total2)

# def function_input(total):
#     while (number_add == 'нет') == True:
#         number_add = input('Можете числа, разделённые пробелом, если напишите слово Нет, то цикл прекратится: ')
#         number_add = number_add.split(' ')
#         number_add = list(number_add)
#         spisok_2 = []
#         for i in number_add:
#             i = int(i)
#             spisok_2.append(i)
#         print(spisok)
#         total_2 = 0
#         for number in spisok_2:
#             total_2 = total + number
#         print(total_2)
#
# function_input(total)

print(('*' * 25), 'Задание №6', ('*' * 25))
slovo = input('Введите слово латиницей с маленькой буквы: ')
def shift():
    return print(slovo.title())
shift()