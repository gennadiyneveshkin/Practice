# Напишите функцию find_median(input_string), которая вычисляет медиану заданного набора чисел.
# Медиана вычисляется так:
# если чисел нечётное количество, медиана — это средний элемент после сортировки;
# если чисел чётное количество, медиана — это среднее арифметическое двух средних элементов после сортировки.


import math


def find_median(input_string):

    # Преобразовываем исходную строку в список с числами, в нем каждый элемент имеет тип str
    input_string = input_string.split()
    print(input_string)

    # Преобразовываем input_string в список с числами, в нем каждый элемент имеет тип int
    input_string = [int(x) for x in input_string]
    print(input_string)

    # Сортируем input_string по возрастанию
    input_string.sort()
    print(input_string)

    # Если количество элементов четное
    if len(input_string) % 2 == 0:

        # Получаем индекс первого среднего элемента
        index_a = int(len(input_string) / 2 - 1) # -1 потому что нумерация индексов идет с 0
        print(index_a)

        # Получаем индекс второго среднего элемента
        index_b = index_a + 1

        # Получаем элемент по их индексам
        a = int(input_string[index_a])
        print(a)
        b = int(input_string[index_b])
        print(b)

        med = (a + b) / 2

    # Есил количество элементов нечетное
    else:

        # Получаем индекс среднего элемента
        index_a = math.floor(len(input_string) / 2) # округляем к меншему, потому что нумерация индексов идет с 0
        print(index_a)

        med = input_string[index_a]

    return med


input_string = '0 1 0 3 12'
print(find_median(input_string))
