# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


from random import randint
n = int(input('Длинна массива:'))
from random import randint
a=[randint(1,100) for i in range(n)]
print(a)
min_el=int(input("Введите минимальное значение:"))
max_el=int(input("Введите максимальное значение:"))
index_list=[]
for i in range(len(a)):
    if min_el <= a[i] <= max_el:
        index_list.append(i)
print(index_list)
