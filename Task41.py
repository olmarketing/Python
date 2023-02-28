# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

# n = int(input('Количество чисел в массиве:'))
# n_list=list(map(int, input(f'Введите через пробел {n} элементов:  ').split()))
# print(*n_list)
# test_trio=[]
# count=0
# for i in range(len(n_list)-2):
#     test_trio=n_list[i:i+3]
#     if test_trio[0]<test_trio[1]>test_trio[2]:
#         count+=1    
# print(count)

n = int(input('Количество чисел в массиве:'))
n_list=list(map(int, input(f'Введите через пробел {n} элементов:  ').split()))
print(*n_list)
n2=len(n_list)
count=0
for i in range(1,n2-1):
    if n_list[i+1]<n_list[i]>n_list[i-1]:
        count+=1    
print(count)
