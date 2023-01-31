# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

import random
n=int(input("Введите количество монеток: "))

mylist=[]
for i in range(n):
    mylist.append(random.randint(0,1))
print(mylist)

orel=0
reshka=0

for i in mylist:
    if i==1:
     orel+=1
    else:
     reshka+=1
if  orel > reshka:
   print(reshka)
else:
   print(orel)   
 