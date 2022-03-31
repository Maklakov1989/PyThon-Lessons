print(('*' * 25), 'Задание №1 к лекции № 6', ('*' * 25))
from time import sleep
class TrafficLight:
    # атрибуты класса
    light_color_stop = 'Красный'
    light_color_wait = 'Желтый'
    light_color_run = 'Зелёный'
    # методы класса
    def running(self):
        print(f"Светофор загорелся красным!!!")
        sleep(7)
        print(f"Светофор загорелся желтым!!!")
        sleep(2)
        print(f"Светофор загорелся зелёным!!!")
        sleep(1.5)
        print(f"Светофор загорелся красным!!!")
tr_l = TrafficLight()
tr_l.running()
print(('*' * 25), 'Задание №2 к лекции № 6', ('*' * 25))
class Road:
    # атрибуты класса
    def __init__(self):
        self.road_length = 5000
        self.road_width = 20
    # методы класса
    def waight(self):
        waight = int(input('Введите массу асфальта на 1 м.кв.: '))
        thickness = int(input('Введите толщину покрытия: '))
        road_waight = self.road_length * self.road_width * waight * thickness
        print("Масса материала, необходимого для покрытия дороги длинной 5 000 м и шириной 20 м.  - ", road_waight)
r = Road()
r.waight()
print(('*' * 25), 'Задание №3 к лекции № 6', ('*' * 25))
class Worker:
    name = "Михалыч"
    surname = "Михалычев"
    position = "Бригадир"
    def __init__(self):
        my_dict = {"wage": 30000, "bonus": 10000}
        self.income = my_dict["bonus"] + my_dict["wage"]
class Position(Worker):
    def get_info(self):
        self.get_full_name = print(Worker.position,'-', Worker.name, Worker.surname)
        self.get_total_income = print('Получает заработную плату - ', self.income, 'руб.')
a = Position()
a.get_info()
