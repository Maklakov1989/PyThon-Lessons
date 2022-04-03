print(('*' * 25), 'Задание №1 к лекции № 7', ('*' * 25))
from random import randint
class Matrix:
    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
    def spisok(self):
        my_list = [randint(self.param_1, self.param_2) for i in range(4)]
        my_list_2 = [randint(self.param_1 + 1, self.param_2 + 1) for i in range(4)]
        my_list_3 = [my_list, my_list_2]
        for el in my_list_3:
            print(el)
m = Matrix(5,8)
print(m.spisok())


