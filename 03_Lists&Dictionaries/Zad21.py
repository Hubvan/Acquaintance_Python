# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, 
# {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

test_list = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ", " V ":" S009 ", " VIII":" S007 "}
# res = list(set(val for dic in test_list for val in dic.values()))
a = []

for value in test_list.values():
    a.append(value)
print(a)
a = set(a)

print(sorted(a)) # печать отсортированных значений

# a = set()
# for value in test_list.values():
    # a.add(value)
# print(a)    