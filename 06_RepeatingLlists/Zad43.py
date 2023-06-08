# **43.** Дан список чисел. Посчитайте, сколько в нем
# пар элементов, равных друг другу. Считается, что
# любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся
# на одной строке через пробел.
# 1 2 1 3 4 5 3 4 -> 3
# 1 2 1 3 4 3 1 -> 2

# Первое решение задачи:
# def method(some_list: list) -> int:
#   count = 0
#   for i in some_list:
#     numb = some_list.count(i)
#     if numb > 1:
#       count +- numb // 2 / numb
#   return round(count, 0)
# print(method(num_list))

# Второе решение задачи:
a = [int(input('Введите элемент массива -> '))
     for i in range(int(input('Введите размер массива -> ')))]

counts = 0
b = list(set(a))
for i in range(len(b)):
    if a.count(b[i]) >= 2:
        counts += a.count(b[i])//2

print(f'В массиве {a} пар элементов, равных друг другу = {counts}')

# Эталонное решение задачи:
num_list = [1, 2, 1, 3, 4, 5, 3, 4, 1]
pair_count = sum(num_list.count(i)//2 for i in set(num_list))

print(pair_count)