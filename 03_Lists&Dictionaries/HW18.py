# Задача 18: 
#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('Введите количество элементов массива: '))
arr = list()
for i in range(n):
   k = int(input('Введите элемент массива: '))
   arr.append(k)

count = 0
x = int(input('Введите искомое число: '))
for i in range(len(arr)):
   if arr[i] == x:
      count += 1
print(f'Искомое число встречается {count} раз') 