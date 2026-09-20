# Дан одномерный массив чисел array, в котором N элементов. Напишите функцию process_array, которая подсчитает,
# сколько чисел в массиве делятся на 3 нацело, и вычислит среднее арифметическое четных чисел.
# Функция process_array должна добавить эти значения в новые элементы на первом и последнем местах в массиве
# соответственно. Верните измененный массив в качестве ответа.
# Например, на вход программы передали массив array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# В нем три элемента делятся нацело на 3, а среднее арифметическое четных чисел — 6.
# В результате должен получиться массив [3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6.0].

# Мой вариант
def process_array(array):
    n = len(array)
    sum = 0
    first = 0
    second = 0
    for i in range(n):
        if array[i] % 3 == 0:
            first += 1
        if array[i] % 2 == 0:
            sum += array[i]
            second += 1
    average = sum / second
    array.insert(0, first)
    array.append(average)
    return array


print(process_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print()

# Вариант Эдюссон

def process_array(array):
    # Подсчитайте количество чисел, которые делятся на 3

    # TODO Дай по единице за каждое число, которое делится на 3, а потом сложи эти единицы
    # TODO sum([1, 1, 1])
    # TODO после помещения спискового включения в круглиые скобки, квадратные уже не обязательны!
    # TODO Хотя если их добавить, все равно будет работать
    count_div_3 = sum(1 for x in array if x % 3 == 0)
    print(count_div_3)

    # Вычислите среднее арифметическое четных чисел
    even_numbers = [x for x in array if x % 2 == 0]
    avg_even = sum(even_numbers) / len(even_numbers) if even_numbers else 0

    # Добавьте значения в массив
    array.insert(0, count_div_3)
    array.append(avg_even)

    return array


print(process_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_div = [1 for x in array if x % 3 == 0]
print(count_div)