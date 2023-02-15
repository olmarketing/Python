# Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def recursive(x,y):
    if y==1:
        return x
    else:
       return x * recursive(x,y-1)
    

a, b = int(input("Введите число a: ")), int(input("Введите число b: "))
print(recursive(a,b))

