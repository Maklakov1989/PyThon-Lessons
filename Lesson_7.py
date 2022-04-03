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
class Clothes:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
