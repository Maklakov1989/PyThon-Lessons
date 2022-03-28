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
print(('*' * 25), 'Задание №2 к лекции № 5(не доделал)', ('*' * 25))
my_f = open('HW_2_2.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(content)
lines = (len(content))
print('Строк в файле - ', lines)
a = str(content)
print('Количество слов в тексте - ', len(set(a.split())))

print(('*' * 25), 'Задание №3 к лекции № 5(не доделал)', ('*' * 25))

f_salary = open('HW_2_3.txt', 'r', encoding='utf-8')
content = f_salary.read()
print(content)
new_list = []
for line in content:
    new_list.append(line)
print(new_list)



