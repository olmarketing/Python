# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел A
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
from random import randint

n=int(input('Введите длину списка: '))

from random import randint
mylist=[randint(1,100) for i in range(n)]
print(mylist)

x = int(input('Введите число:'))
print(mylist.count(x))
