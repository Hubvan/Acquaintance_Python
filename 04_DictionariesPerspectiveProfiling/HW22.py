# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать 
# без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств.

a = [int(x) for x in input('Введите элементы первого множества: ').split()]
k = set(a)

b = [int(x) for x in input('Введите элементы второго множества: ').split()]
k1 = set(b)

lok = k & k1
print(f'Числа встречающиеся в обоих наборах: {lok}')

# nums1 = [3, 2, 1, 1, 4]
# nums2 = [3, 10, 5, 1]

# result = sorted(set(nums1).intersection(set(nums2))) # во множествах данные определенных типов сортируются автоматически
# print(result) 