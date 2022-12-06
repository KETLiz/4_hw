# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

n = int(input('Введите число: '))
count = 2
list = []

while count < n:
    if n % count == 0:
        list.append(count)
    count += 1
    
print(list)