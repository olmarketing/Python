# Задача №5. Решение в группах Вагоны в электричке пронумерованы натуральными числами,
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
#это зависит от того, в какую сторону едет электричка). 
#В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
#что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. 
#Напишите программу, которая будет это делать или сообщать, 
#что без дополнительной информации это сделать невозможно. 
#Input: 3 4(ввод на разных строках) 
#Output: 6

i = 3
j = 4

if (i == j):
    print('Решения нет')
else:
    print(i+j-1)

# i = int(input("Введите № от головы поезда: "))

# j = int(input("Введите № вагона: "))

# if i != j:
#     wagons = j + i-1
#     print(f"Всего вагонов: {wagons}")
# else:
#     print(
#         f"Нужна дополнительная информация, является ли {j} номером от хвоста")
#     tail = int(
#         input(f"Введите 1 если {j} - является номером хвоста, 0 если нет: "))
#     if tail == 1:
#         wagons = j + i-1
#         print(f"Всего вагонов: {wagons} ")
#     else:
#         print(f"Решения нет")