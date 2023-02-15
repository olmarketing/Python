# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4


def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)
 
a, b = int(input("Введите число a: ")), int(input("Введите число b: "))
if a<0 or b<0:
    print("Здесь есть отрицательные числа!")
 
summa=sum(a, b)
print('Сумма чисел =', summa)