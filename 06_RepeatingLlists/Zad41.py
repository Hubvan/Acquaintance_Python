# **41.** Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве
# определит количество элементов, у которых два
# соседних и, при этом, оба соседних элемента меньше данного.
# Массив чисел вводится в одну строку через пробел.
# Массив состоит из целых чисел.
# Пример:
# 5 1 3 7 9 6 -> 1
# 3 4 3 6 5 8 7 -> 3

# def method(some_list: list) ->int:
#   count = 0
#   for i in range(1, len(some_list) - 1):
#     if some_list[i] > some_list[i - 1] and some_list[i] > some_list[i + 1]:
#       count +
#   return count
# print(method(num_list))



num_list = [3, 4, 3, 6, 5, 8, 7]
print(len([num_list[i] for i in range(1, len(num_list)-1)
          if (num_list[i] > num_list[i+1] and
              num_list[i] > num_list[i-1])]))