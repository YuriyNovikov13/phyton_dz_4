# 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
import sympy


num = int(input('Введите степень многочлена, это должно быть целое число: '))

# def get_polynomial(num:int)->str:
#     '''
#     Создание многочлена 
#     '''
#     x = sympy.Symbol('x')
#     expr = 0
#     for i in range(num + 1):
#         a = random.randint(0, 100)
#         if a == 1:
#             expr += x ** i
#         if a != 0:
#             expr += a * x ** i
#     expr = str(expr) + ' = 0'    
#     return expr
x = sympy.Symbol('x')
expr = 0
for i in range(num + 1):
    a = random.randint(0, 10)
    if a == 1:
            expr += x ** i
    if a != 0:
            expr += a * x ** i
expr = str(expr) + ' = 0'    
print (expr)
    
f = open('file_04_04.txt', 'w')
f.write(expr)
f.close()

