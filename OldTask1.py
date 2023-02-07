

# # Напишите программу, которая принимает на вход цифру, 
# # обозначающую день недели, и проверяет, является ли этот день выходным.
# # Пример:
# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет

# dayweek=int(input('Введите номер дня недели: '))
# if dayweek<1 or dayweek>7:
#     print('Такого дня недели не существует')
# elif dayweek==6 or dayweek==7:
#     print('Этот день выходной')
# else:
#     print('Это день рабочий')

# Перевод в список, кортеж
my_list = [2,3,5,7,4,3,5,3,2,45,6,3,12,5,7,4,5]
new_set = set(my_list)
new_list = list(set(my_list))
new_tuple = tuple(set(my_list))
cur_tuple = new_tuple[:-3]
new_tuple = cur_tuple