print(('*' * 25), 'Задание №1', ('*' * 25))

def devide(number_1, number_2):
    try:
        return round(number_1 / number_2, 2)
    except: ZeroDivisionError
number_1 = int(input('Введите 1 число: '))
number_2 = int(input('Введите 2 число: '))
print(f'Число 1 делить на число 2 равно - {devide(number_1, number_2)}')
print(('*' * 25), 'Задание №2', ('*' * 25))
def person():
    return print(name,surname, date_of_birth, city, e_mail, tel)
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
date_of_birth = input('Введите дату рождения: ')
city = input('Введите место рождения: ')
e_mail = input('Введите e-mail: ')
tel = input('Введите телефон: ')
person()
print(('*' * 25), 'Задание №3', ('*' * 25))
def max_func():
    s = max(x)
    x.remove(s)
    s2 = max(x)
    print('Два максимальных числа из введённых: ', s, 'и', s2)
    return s + s2
a = int(input('Введите значение 1: '))
b = int(input('Введите значение 2: '))
c = int(input('Введите значение 3: '))
x = [a, b, c]
print(f'Сумма максимальных 2-х значений из введённых - {max_func()}')
print(('*' * 25), 'Задание №4', ('*' * 25))
x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))
"""Возведение в степень встроенной командой"""
def my_func_1 (x, y):
        return x**y
print(f'Результат функции 1: {my_func_1(x, y)}')
"""Возведение в степень без встроенной команды"""
i = 1
def my_func_2 (x, y):
    for i in range(abs(x)):
        i = y
        i = 1/(x * x)
        return i
print(f'Результат функции 2: {my_func_2(x, y)}')

print(('*' * 25), 'Задание №5', ('*' * 25))
numbers = None
def numbers_summ():
    numbers = input('Введите числа, разделённые пробелом: ')
    numbers = numbers.split(' ')
    numbers = list(numbers)
    spisok = []
    for i in numbers:
        i = int(i)
        spisok.append(i)
    print('Вы ввели - ', spisok)
    total = 0
    for number in spisok:
        total = total + number
    print(f'Сумма введённых чисел - {total}')
    print('Хотите продолжить? y/n')
    a = input()
    f = []
    while a == 'y':
        print('Введите числа через пробел: ')
        d =(input())
        d = d.split(' ')
        d = list(d)
        for i in d:
            i = int(i)
            f.append(i)
        print('Список новых чисел - ', f)
        for number in f:
            total = total + number
        print(f'Cумма всех введённых чисел - {total}')
        print('Хотите продолжить y/n')
        a = input()
    if a == 'n':
        print('Задание завершено! Спасибо!!')
    return total
print('Сумма всех введённых чисел - ', numbers_summ())

print(('*' * 25), 'Задание №6', ('*' * 25))
slovo = input('Введите слово латиницей с маленькой буквы: ')
def shift():
    x = slovo.title()
    print('Введённое слово с большой буквы - ', x)
    print(('*' * 25), 'Задание №7', ('*' * 25))
    print('Хотите ввести еще слова? y/n')
    a = input()
    f = []
    f.append(x)
    while a == 'y':
        print('Введите несколько слов через пробел: ')
        d = (input())
        d = d.title()
        d = d.split(' ')
        for el in d:
            f.append(el)
        print('Новые слова с большой буквы - ', d)
        print('Список всех введенных слов:', f)
        print('Хотите продолжить? y/n')
        a = input()
    if a == 'n':
        print('Задание завершено! Спасибо!!')
shift()

