print(('*' * 25), 'Задание №1 к лекции № 7', ('*' * 25))
class Matrix:
    def __init__(self, param_1, param_2, param_3):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
    def spisok(self):
        self.my_list = [self.param_1, self.param_2, self.param_3]
        for el in self.my_list:
            print(el)
    def __str__(self):
        return f'Выми были введены 2 числа {self.param_1}, {self.param_2} и {self.param_3} из которых в случайном порядке ' \
               f'была сделана матрица 2х4'
m = Matrix([5, 8], [6, 9], [4, 1])
print(m.spisok())
print(m.__str__())