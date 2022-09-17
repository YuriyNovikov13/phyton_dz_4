# 3 Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random

number = int(input('Введите размер списка, это должно быть целое число: '))
list_num = [random.randint(0, 10) for _ in range(number)]
list_uique = []

for i in list_num:
    if i in list_uique:
        continue
    list_uique.append(i)

print('Исходный список', list_num)
print(list_uique)
