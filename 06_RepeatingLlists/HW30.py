# Задача 30: Заполните массив элементами арифметической прогрессии. Её
# первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input())
# d = int(input())
# n = int(input())
# for i in range(n):
#   print(a1 + i * d)

a1 = int(input('Первый член прогрессии: '))
n = int(input('Количество членов прогрессии: '))
d = int(input('Разность: '))
progression = [a1 + (i-1)*d for i in range(1, n+1)]
new_prog = []
for i in range(1, n+1):
  elem = a1 + (i-1)*d
  new_prog.append(elem)
print('new_prog: ', new_prog)
print(progression)