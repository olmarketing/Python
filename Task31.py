# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  a0= 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


def Fibonacci(n: int):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1 
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

# n=int(input('Введите число: '))
# for i in range(n):
#     num_fib=Fibonacci(i)
#     print(i+1,'-', num_fib)
# print(i+1,'число Фибоначчи -', num_fib)

n=int(input('Введите число: '))
print(n,'число Фибоначчи -', Fibonacci(n-1))