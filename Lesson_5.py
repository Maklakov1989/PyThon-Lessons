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
my_f = open('HW_2.txt', 'r', encoding='utf-8')
content = my_f.readlines()
print(content)
lines = (len(content))
print('Строк в файле - ', lines)




