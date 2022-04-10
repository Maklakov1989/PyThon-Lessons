print(('*' * 25), 'Задание №1 к лекции № 8', ('*' * 25))
class Date:
    @classmethod
    def get_day(cls, param):
        x = param.split('-')
        my_dict = {'первое' : "01", 'второе' : "02", 'третье' : "03", 'четвёртое' : "04", 'пятое' : "05",
                   'шестое' : "06", 'седьмое' : "07", 'восьмое' : "08", 'девятое' : "09", 'десятое' : "10"}
        day = my_dict[x[0]]
        print(f'Введённое пользователем число - {day}')
    @staticmethod
    def get_month(param):
        x = param.split('-')
        my_dict_2 = {'января': "01", 'февраля': "02", 'марта': "03", 'апреля': "04", 'мая': "05",
                   'июня': "06", 'июля': "07", 'августа': "08", 'сентября': "09", 'октября': "10",
                   'ноября': "11", 'декабря': "12"}
        month = my_dict_2[x[1]]
        print(f'Введённый пользователем месяц - {month}')
Date.get_day("десятое-декабря-2010")
Date.get_month("десятое-декабря-2010")
print(('*' * 25), 'Задание №2 к лекции № 8', ('*' * 25))
class my_exeption(ZeroDivisionError):
    def __init__(self, param):
        self.param = param
    try:
        param = input('Введите число, которое мы будем делить на 0: ')
        y = param / 0
    except:
        print("А делить на ноль нельзя!!")
print(('*' * 25), 'Задание №3 к лекции № 8', ('*' * 25))
class Str_exeption(Exception):
    def __init__(self, list):
        self.list = list
inp_data = input("Введите любые значения: ")
inp_data = inp_data.split(' ')
res = []
for item in inp_data:
    try:
        res.append(int(item))
    except ValueError:
        pass
print('Введены числа - ', res)
print('Хотите продолжить? y/n')
a = input()
f = []
while a == 'y':
    add_data = input('Введите любые значения через пробел: ')
    add_data = add_data.split(' ')
    for item in add_data:
        try:
            res.append(int(item))
        except ValueError:
            pass
    print('Список новых чисел - ', res)
    print('Хотите продолжить y/n')
    a = input()
    if a == 'n':
        print('Задание завершено! Спасибо!!')
print(('*' * 25), 'Задание №4,5,6 к лекции № 8', ('*' * 25))
print("")
class OfficeEquipmentWarehouse:
    print("Склад оргтехники")
class OfficeEquipment:
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color
class Printer(OfficeEquipment):
    amount_pr = 0
    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1
    @staticmethod
    def name():
        return "Принтер: "
    def type_printer(self):
        return self.pr_type
    def __str__(self):
        return f"    производитель: {self.producer}     цвет: {self.color}      тип принтера: {self.pr_type}"
class Scanner(OfficeEquipment):
    amount_sc = 0
    def __init__(self, producer, color, sc_speed):
        super().__init__(producer, color)
        self.sc_speed = sc_speed
        Scanner.amount_sc += 1
    @staticmethod
    def name():
        return"Сканер: "
    def type_speed(self):
        return self.sc_speed
    def __str__(self):
        return f"    производитель: {self.producer}     цвет: {self.color}     скорость сканирования: {self.sc_speed} стр/мин"
class Notepad(OfficeEquipment):
    amount_n = 0
    def __init__(self, producer, color, nb_wi_fi):
        super().__init__(producer, color)
        self.nb_wi_fi = nb_wi_fi
        Notepad.amount_n += 1
    @staticmethod
    def name():
        return "Ноутбук: "
    def wi_fi_module(self):
        return self.nb_wi_fi
    def __str__(self):
        return f"    производитель: {self.producer}     цвет: {self.color}       Wi-Fi модуль: {self.nb_wi_fi}"
p = Printer('Canon', 'белый', 'струйный')
p2 = Printer('Hp', 'серый', 'лазерный')
p3 = Printer('Wanhao', 'серый', '3D')
print(p.name(), p.amount_pr, "шт")
print(p.__str__())
print(p2.__str__())
print(p3.__str__())

s = Scanner('Epson', 'черный', '1')
s2 = Scanner('Avision', 'белый', '2')
s3 = Scanner('Kodak', 'желтый', '3')
s4 = Scanner('HP','серый','4')
print(s.name(), s.amount_sc, "шт")
print(s.__str__())
print(s2.__str__())
print(s3.__str__())
print(s4.__str__())

n = Notepad('Lenovo', 'черный', 'есть')
n2 = Notepad('Acer', 'золотой', 'есть')
n3 = Notepad('HP', 'серый', 'есть')
n4 = Notepad('Apple', 'серебро', 'отсутствует')
print(n.name(), n.amount_n, "шт")
print(n.__str__())
print(n2.__str__())
print(n3.__str__())
print(n4.__str__())
print(('*' * 25), 'Задание №7 к лекции № 8', ('*' * 25))
class ComplexNum:
    num_of_numbers = 0
    def __init__(self, re, im):
        self.re = re
        self.im = im
        ComplexNum.num_of_numbers += 1
    def __del__(self):
        print(f'Удалили число {self.re} + i*{self.im}')
    def __str__(self):
         return f"Комплексное число {self.re} + i*{self.im}"
    def __add__(self, other):
        return ComplexNum(self.re + other.re, self.im + other.im)
    def __eq__(self, other):
        return self.re == other.re and self.im == other.im
    @staticmethod
    def my_method():
        return f"Количество чисел - {ComplexNum.num_of_numbers}"
    @classmethod
    def class_method(cls):
        return(f'Инициализировано {ComplexNum.num_of_numbers} класса {cls}')