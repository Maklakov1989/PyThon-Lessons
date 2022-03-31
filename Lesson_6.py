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
    road_length = 'Красный'
    road_width = 'Желтый'
    light_color_run = 'Зелёный'
