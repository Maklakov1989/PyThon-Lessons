print(('*' * 25), 'Задание №1 к лекции № 4', ('*' * 25))
from sys import argv
skript_name, hours, rate, bonus = argv
print(f'Часов отработано - {hours}')
print(f'Часовая ставка - {rate}')
print(f'Премия - {bonus}')
salary = (int(hours) * int(rate)) + int(bonus)
print(f'Заработная плата в месяц {salary}')
print(('*' * 25), 'Задание №2 к лекции № 4 НЕ ГОТОВО!!!!', ('*' * 25))
from random import randint
my_list = []
for i in range(12):
    my_list.append(randint(1, 10))
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Дан случайный список - {my_list}')
new_list = []
for i in my_list:
    if my_list[i] > my_list[i - 1]:
        new_list.append(i)
print(f'Новый список с элементами больше предудущего: {new_list}')
print(('*' * 25), 'Задание №3 к лекции № 4', ('*' * 25))
my_list = range(20,240)
new_list = [el for el in my_list if el % 21 == 0 or el % 20 == 0]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
print(('*' * 25), 'Задание №4 к лекции № 4', ('*' * 25))
from random import randint
my_list = []
for i in range(12):
    my_list.append(randint(1, 10))
print(f'Дан случайный список - {my_list}')
new_list = []
for el in my_list:
    b = 0
    for i in my_list:
        if el == i:
            b += 1
    if b == 1:
        new_list.append(el)
print('Элементы не имеющие повторений - ', new_list)
print(('*' * 25), 'Задание №5 к лекции № 4', ('*' * 25))
from functools import reduce
from random import randint
my_list = []
for i in range(12):
    my_list.append(randint(100, 1000))
print(f'Дан случайный список - {my_list}')
def my_func(prev_el, el):
    """prev_el - предыдущий элемент, el - текущий элемент"""
    return prev_el + el
print(f'Произведение всех элементов списка - ', reduce(my_func, my_list))
print(('*' * 25), 'Задание №6 к лекции № 4 НЕ ГОТОВО!!!!', ('*' * 25))
from sys import argv
skript_name, start_number, random_number = argv
print(('*' * 25), 'Задание №7 к лекции № 4 НЕ ГОТОВО!!!!', ('*' * 25))

