# 2. Создайте класс, который будет наследоваться от списка. Сделайте так, чтоб у вашего списка можно было вычесть другой список.
class NevList(list):
    def __sub__(self, other):
        return NevList(x for x in self if x not in other)

list1 = NevList([1, 2, 3, 4, 5, 6, 'pip', 'Monti'])
list2 = NevList([2, 4, 'pip'])
print(list1 - list2)