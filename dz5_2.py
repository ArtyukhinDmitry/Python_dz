# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4 

print('Введи a : ')
a = int(input())
print('Введи b : ')
b = int(input())

# c = int
# def sum(c):
#     return a+b
# print(sum(c))

def sum(a, b):
    if a<0 or b<0:
        return 'error'
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return sum(a, b-1) + 1
    else:
        return sum(a-1, b) + 1

print(sum(a, b))


