# Вывести на экран таблицу умножения

# Мой вариант

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1 = [' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for el in numbers1:
    print(el,'',end ='')
print()

for el in numbers:
    print(el,'',end ='')
    for i in range (1, 11):
        print(el*i,'',end ='')
    print()

print('\n')

# Вариант Эдюссон
# Этот код создает двумерный список таблицы умножения.
a0 = [' ', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [a0, a1]
for i in range(2, 11):
    ai = []
    for j in a1:
        j = j * i
        ai.append(j)
    a.append(ai)

# Этот код выводит таблицу умножения на экран.
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()