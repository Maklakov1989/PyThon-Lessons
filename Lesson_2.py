print(('*' * 25), 'Задание №1', ('*' * 25))

spisok = [2, 'слово', {'словарь'}, ['список']]
print(spisok)
for element in spisok:
    print(element, '--', type(element))
print(('*' * 25), 'Задание №2', ('*' * 25))

my_list = input('Введите 4 чисела через пробел: ')
my_list = my_list.split(' ')
my_list = list(my_list)
print(type(my_list))
print(my_list)

i = 1
for i in range(0, len(my_list), 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i + 1

print(my_list)

print(('*' * 25), 'Задание №3', ('*' * 25))
month = (input('Введите число от 1 до 12: '))
mm = {'1':'Зима', '2':'Зима','3':'Весна','4':'Весна','5':'Весна','6':'Лето','07':'Лето','8':'Лето','9':'Осень',
      '10':'Осень','11':'Осень','12':'Зима'
}
print('это будет - ', mm[month])
print(('*' * 25), 'Задание №4', ('*' * 25))
words = input('Введите несколько слов через пробел: ')
words_list = words.split(' ')
count = 0
for i in range(1, len(words_list)+1):
    print(i, ')', words_list[i-1])
print(('*' * 25), 'Задание №5', ('*' * 25))
my_list = [7, 5, 3, 3, 2]
print(my_list)
y = None
x = 1
for x in my_list:
    x = int(input('Введите число больше 0 (0 прекращает цикл): '))
    my_list.append(x)
    y = (sorted(my_list))
    print(f'Пользователь ввёл число {x}, Результат: {y}')
    if x == 0:
        print('Всё')
        break
print(('*' * 25), 'Задание №6', ('*' * 25))
list_6 = []
dict1 = {
}
product = input('Введите тип товара: ')
price = input('Введите цену товара: ')
quont = input('Введите количество товара: ')
unit = input('Введите ед. измерения товара: ')
dict1['Тип товара'] = product
dict1['Цена'] = price
dict1['Количество'] = quont
dict1['Единица измерения'] = unit
dict2 = {
}
product = input('Введите тип товара: ')
price = input('Введите цену товара: ')
quont = input('Введите количество товара: ')
unit = input('Введите ед. измерения товара: ')
dict2['Тип товара'] = product
dict2['Цена'] = price
dict2['Количество'] = quont
dict2['Единица измерения'] = unit
dict3 = {
}
product = input('Введите тип товара: ')
price = input('Введите цену товара: ')
quont = input('Введите количество товара: ')
unit = input('Введите ед. измерения товара: ')
dict3['Тип товара'] = product
dict3['Цена'] = price
dict3['Количество'] = quont
dict3['Единица измерения'] = unit

position = (1, dict1, 2, dict2, 3, dict3)
list_6.append(position)
print(list_6)
product_dict = {
}
product_dict.update({'Название' : [dict1.get('Тип товара'), dict2.get('Тип товара'), dict3.get('Тип товара')],
'Цена' : [dict1.get('Цена'), dict2.get('Цена'), dict3.get('Цена')],
'Количество' : [dict1.get('Количество'), dict2.get('Количество'), dict3.get('Количество')],
'Ед' : [dict1.get('Единица измерения'), dict2.get('Единица измерения'), dict3.get('Единица измерения')]})
print(product_dict)
