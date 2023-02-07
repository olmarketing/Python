# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint
n = int(input('Длинна массива:'))
from random import randint
a=[randint(1,100) for i in range(n)]
print(a)
x = int(input('Заданное число:'))

b=[abs(a[i]-x) for i in range(len(a))]
print(a[b.index(min(b))])
