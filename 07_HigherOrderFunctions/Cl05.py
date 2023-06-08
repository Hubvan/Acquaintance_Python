# Файлы

# 1. Режим a

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a', encoding='utf-8') # здесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

# Режим r
# Чтение данных из файла:
path = 'file.txt'
data = open(path, 'r')
for line in data:
  print(line)
data.close()