# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

print('Введи a : ')
a = int(input())
print('Введи b : ')
b = int(input())

# def degree(b):
#     if b == 0:
#         return 1
#     return a**b
# print(degree(b))

def degree(a, b):
    if b == 0:
        return 1
    return degree(a, b-1)*a

print(degree(a, b))

