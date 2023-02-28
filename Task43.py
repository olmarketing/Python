# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

# from random import randint
# n = int(input('Введите количество чисел:'))
# from random import randint
# a=[randint(1,100) for i in range(n)]
# print(a)

# n = int(input('Количество чисел в массиве:'))

# def Dcount(n_list):
#     couple=0
#     for i in range(1,len(n_list)):
#         if n_list[i]==n_list[i-1]:
#             couple+=1
#     print(couple)

# n_list=list(map(int, input(f'Введите через пробел  элементов:  ').split()))
# n_list.sort()
# print(*n_list)
# Dcount(n_list)

arr=[1,1,1,1,1]
n=len(arr)
result=0
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]==arr[j]:
            result+=1
print(f'{arr} Пары = {result}')            
