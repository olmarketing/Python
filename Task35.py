# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def Simple_number(x):
    # nums=list(range(2,x))
    # for i in nums:
    for i in range(2,x):
        if x%i==0:
            return "No"
    return "Yes"

n=int(input('Введите число: '))
print(Simple_number(n))

    
