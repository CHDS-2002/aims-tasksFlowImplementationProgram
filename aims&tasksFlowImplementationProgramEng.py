# os - library for working with the console

import os

# Setting the font color of the console
os.system('COLOR B')

print('Hi, PyCharm')  # The output is 'Hi, PyCharm'
x = 43  # x - number
y = 32  # y - number
print(x * y)  # Output x * y
print("End line")  # Output of the 'End line'

try:
    os.system('PAUSE')  # Stopping the program
    os.system('CLS')  # Clearing the console screen
except:
    os.system('CLS')  # Clearing the console screen
