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
print(('*' * 25), 'Задание №3 к лекции № 5', ('*' * 25))
with open('HW_2_3.txt', 'r', encoding='utf-8') as my_file:
    task_3 = []
    zp = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            zp.append(i[0])
        task_3.append(i[1])
print(f'Оклад меньше 20.000 {zp}, средний оклад {sum(map(int, task_3)) / len(task_3)}')
my_file.close()
print(('*' * 25), 'Задание №4 к лекции № 5', ('*' * 25))
my_dict = {'One' : "Один", 'Two' : "Два",'Three' : "Три",'Four' : "Четыре"}

with open('HW_2_4.txt', 'r', encoding='utf-8') as my_file:
    task_3 = []
    perevod = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        i.remove('—')
        print(i)
        print([my_dict[i[0]], i[1]])
my_file.close()

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



