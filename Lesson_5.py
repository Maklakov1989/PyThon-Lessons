print(('*' * 25), 'Задание №1 к лекции № 5', ('*' * 25))

f_obj = open("HomeWork.txt", 'a')

while words != (" "):
    words = str(input("\n Введите текст: "))
    break
f_obj.write(text)
print(f_obj.read())
f_obj.close()