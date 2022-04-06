print(('*' * 25), 'Задание №1 к лекции № 7', ('*' * 25))
class Matrix:
    def __init__(self, param_1, param_2, param_3):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
    def spisok(self):
        self.my_list = [self.param_1, self.param_2, self.param_3]
        print(self.my_list)
    def __str__(self):
        return f'\n{self.param_1}, {self.param_2}, {self.param_3}'
    def __add__(self, other):
        return Matrix(self.param_1 + other.param_1,
                      self.param_2 + other.param_2,
                      self.param_3 + other.param_3)
m = Matrix(5, 8, 9)
m2 = Matrix(6, 9, 2)
m3 = Matrix(2, 4, 1)
print(m.spisok(), m2.spisok(), m3.spisok())
print(m.__str__(), m2.__str__(), m3.__str__())
print(m + m2 + m3)
print(('*' * 25), 'Задание №2 к лекции № 7', ('*' * 25))
from abc import ABC
class Clothes(ABC):
    def __init__(self, size):
        self.size = size
class Coat(Clothes):
    def __init__(self, size):
        self.size = size
    @property
    def Coat_consumption(self):
        return f"Для размера пальто {self.size}, необходимо:" \
        f" {round(self.size/6.5, 2) + 0.5} м. материала"
class Jacket(Clothes):
    def __init__(self, size):
        self.size = size
    @property
    def Jacket_consumption(self):
        return f"Для размера костюма {self.size}, необходимо:" \
        f" {round(2*self.size, 2) + 0.3} м. материала"
j = Jacket(52)
c = Coat(43)
print(c.Coat_consumption)
print(j.Jacket_consumption)
print(('*' * 25), 'Задание №3 к лекции № 7', ('*' * 25))
class Cell:
    def __init__(self, quont):
        self.quont = quont
        self.cell = []
    def __add__(self, other):
        return Cell(self.quont + other.quont)
    def __sub__(self, other):
        if self.quont - other.quont > 0:
            return f'Произошло объединение клеток {Cell(self.quont - other.quont)}'
        else:
            return 'Что-то пошло не так, отрицательное количество ячеек!!!'
    def __mul__(self, other):
        self.cell.append(Cell(self.quont * other.quont))
        if self.cell != None:
            return f'Cоздана новая клетка {Cell(self.quont * other.quont)}'
        else:
            return 'Ничего не произошло'
    def __truediv__(self, other):
        self.cell.append(Cell(round(self.quont / other.quont, 0)))
        return f'Cоздана новая клетка делением {Cell(round(self.quont / other.quont, 0))}'
    def __str__(self):
        return f"клетка с количеством ячеек ({self.quont})"

c_1 = Cell(5)
c_2 = Cell(6)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)