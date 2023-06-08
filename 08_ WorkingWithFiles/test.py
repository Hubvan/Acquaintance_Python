with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('Privet, mir')

with open('test.txt', 'a', encoding='utf-8') as file:
    file.write('\nPrivet,mir! \nPrivet,mir!')

with open('test.txt', 'r', encoding='utf-8') as file:
    print(file.read())

with open('test.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

data[1] = 'new string\n'

print(data)
with open('test.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)

#print(file.read())