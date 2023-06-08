# Импорт модуля:
# Вариант 1: Импорт файла с функцией

import modul1

print(modul1.max1(5, 9))

# Вариант 2: Импорт функции из файла

from modul1 import max1

print(modul1.max1(10, 9))

# Вариант 3: Импорт из файла все функции

from modul1 import *

print(modul1.max1(10, 9))

# Вариант 3: Импорт и переименование файла все функции

import modul1 as m1

