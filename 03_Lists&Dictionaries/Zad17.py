# Дан список чисел. Определить, сколько в нем встречается различных чисел.
# list_1 = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

a = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]
b = []

for temp in a:
    if (not temp in b):
        b.append(temp)
print(len(b))

print(len(set(a)))