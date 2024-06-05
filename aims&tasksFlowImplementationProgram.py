# os - библиотека для работы с консолью

import os

# Зададим цвет шрифта консоли
os.system('COLOR B')

print('Hi, PyCharm')  # Вывод 'Hi, PyCharm'
x = 43  # x - число
y = 32  # y - число
print(x * y)  # Вывод x * y
print("End line")  # Вывод 'End line'

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
