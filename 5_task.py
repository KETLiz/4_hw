# 5'. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
import sympy

with open('file1.txt', 'w') as data:
    data.write('2*x**2 + 4*x + 5')
    
with open('file2.txt', 'w') as data:
    data.write('4*x**2 + 1*x + 4')

with open('file1.txt', 'r') as data:
    file1 = data.readline()
    list_file1 = file1.split()
   
with open('file2.txt', 'r') as data:
    file2 = data.readline()
    list_file2 = file2.split()

with open('sum_of_polynoms.txt', 'w') as data:
    data.write(f'{list_file1} + {list_file2}')