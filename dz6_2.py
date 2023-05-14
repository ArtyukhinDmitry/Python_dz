# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

n = int(input('Введи кол-во элементов массива: '))
n1 = int(input('Введи min: '))
n2 = int(input('Введи max: '))

import random
list1 = [random.randint(-5, 20) for i in range(n)]
print(list1)

for i in range(len(list1)):
    if n2 >= list1[i] >= n1:
        print('Результат: ', i)