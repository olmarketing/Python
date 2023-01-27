#В некоторой школе решили набрать три новых
#математических класса и оборудовать кабинеты для
#них новыми партами. За каждой партой может сидеть
#два учащихся. Известно количество учащихся в
#каждом из трех классов. Выведите наименьшее
#число парт, которое нужно приобрести для них.
#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32

a = 20
b = 21
c = 22

def Tables(a):
    res=a//2 + a%2
    return res
print(Tables(a) + Tables(b) + Tables(c))

# a = 20
# b = 21
# c = 22
# print(a//2 + a%2 + b//2 + b%2 + c//2 + c%2)

# classes = []
# for i in range(3):
#     students = int(input(f'Введите количество учеников в {i + 1} классе: '))
#     classes.append(students)

# total_desks = 0

# for c in classes:
#     total_desks += c // 2 + c % 2

# print(f'Минимальное количество парт: {total_desks}')

# import math 

# classes = int(input('Введите количество классов: '))
# desks = 0
# for i in range(classes):
#     a = int(input(f'Введите количество учащихся в {i+1} классе: ')) # счётчик с нуля , поэтому +1
#     desks += math.ceil(a/2) # округление в большую сторону

# print (f'Миниально нужно {desks} парт')

