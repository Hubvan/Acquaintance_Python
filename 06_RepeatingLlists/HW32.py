# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#   if min_number <= max_number:
#     print(i)

start_d, end_d = (int(input('Начало диапозона: ')),
                  int(input('Конец диапазона: ')))
# получаем на вход список чисел
num_list = list(map(int, input().split()))
# генерация результирующего списка
# в список  попадают индексы элементов, для которых выполняется условие задачи
result = [i for i in range(len(num_list)) if (num_list[i] <= end_d
                                              and num_list[i] >= start_d)]

print(result)