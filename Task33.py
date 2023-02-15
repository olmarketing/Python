# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint
n = int(input('Количество оценок:'))
from random import randint
estimates=[randint(1,5) for i in range(n)]
print(estimates)

# def max_number(list1: list):
#     max_number=max(list1)
#     min_number=min(list1)
#     for i in list1: 
#         if list1[i]==max_number:
#             list1[i]=min_number
#     return list1
# max_number(estimates)
# print(estimates)

max_number=max(estimates)
min_number=min(estimates)

for i in range(len(estimates)): 
        if estimates[i]==max_number:
            estimates[i]=min_number
   
print(estimates)