# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10 в 5 степени.
# Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

k=int(input('Введите натуральное число: '))

my_dict = dict()
for i in range(1, k+1):
    my_dict[i]=1
    for j in range(2, (i//2)+1):
           if i % j==0:
             my_dict[i] +=j

for i in range(1, len(my_dict)+1):
        for j in range(i+1, len(my_dict)+1):
            if i==my_dict[j] and j==my_dict[i]:
                print(i,j)
         




