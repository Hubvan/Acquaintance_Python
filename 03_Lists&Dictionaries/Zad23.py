# Задача №23.
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

arr = [0, -1, 5, 2, 3, 4, 0]
count = 0

for x in range(1, len(arr)):
    if arr[x-1] < arr[x]:
        count += 1
print(count) 