# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input('Введи а: '))
n = int(input('Введи n: '))
d = int(input('Введи d: '))
for i in range(n):
    print('Результат: ', a1 + i * d)