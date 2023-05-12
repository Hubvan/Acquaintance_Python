# Задача 26: 
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А 
# в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def exponentiation(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * exponentiation(a, b - 1)
    
a1 = int(input("Введите число a: "))
b1 = int(input("Введите число b: "))

print(f"{a1} в степени {b1} равно {exponentiation(a1, b1)}")