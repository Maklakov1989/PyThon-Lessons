print(('*' * 25), 'Задание №1 к лекции № 5', ('*' * 25))
text = []
while True:
    line = input('Введите текст: ')
    text.append(line)
    if line == "":
        break
print('Вы ввели: ', text)
f_obj = open("HomeWork.txt", 'a')
for line in text:
    f_obj.write(line + '\n')
f_obj.close()
print(('*' * 25), 'Задание №2 к лекции № 5', ('*' * 25))
my_f = open('HW_2_2.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(content)
lines = (len(content))
print('Строк в файле - ', lines)
a = str(content)
print('Количество слов в тексте - ', len(set(a.split())))
f_obj.close()
print(('*' * 25), 'Задание №3 к лекции № 5(не доделал)', ('*' * 25))
f_salary = open('HW_2_3.txt', 'r', encoding='utf-8')
list = []
data = []
for el_1 in f_salary.readlines():
    el_2 = el_1.split(' ')
    list.append(el_2)
print(('*' * 25), 'Задание №4 к лекции № 5(не доделал)', ('*' * 25))
print(('*' * 25), 'Задание №5 к лекции № 5', ('*' * 25))
numbers = input('Введите числа через пробел: ')
f_obj = open("HW_2_5.txt", 'a')
f_obj.write('Пользователь ввёл чиcла - ' + numbers + '\n')
numbers = list(numbers.split(' '))
print('Вы ввели: ', numbers)
sum_list = []
for i in numbers:
    i = int(i)
    sum_list.append(i)
from functools import reduce
def my_func(prev_el, el):
    return prev_el + el
x = reduce(my_func, sum_list)
print('Сумма всех элементов', x)
f_obj.write(f'Сумма всех элементов {x}')
f_obj.close()



