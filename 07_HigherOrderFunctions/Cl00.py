def f(x):
    return x * x

print(f(5))
print(type(f))
a = f
print(a(5)) # a - это переменная которая хранит в себе ссылку на функцию f
print(type(a))



def calk2(a, b):
  return a * b

def math(op, x, y): # в функцию math передаётся два аргумента функция op и аргумент x
  print(op(x, y))

# def calk1(a, b): 
#   return a + b

# Лямбда функция: # преобразуем вышестоящую функцию
calk1 = lambda a, b: a + b

math(calk1, 5, 45)

# второй вариант сокращения:

math(lambda a, b: a + b, 5, 45)