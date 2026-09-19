# Напишите функцию sum_excluding_multiples(n), которая возвращает сумму чисел от 0 до n (включительно),
# не считая чисел, делящихся на 3 или на 7.

def sum_excluding_multiples(n):
    sum_n = 0
    for i in range (n + 1):
        if i % 3 != 0 and i % 7 != 0:
            sum_n = sum_n + i
    return sum_n
