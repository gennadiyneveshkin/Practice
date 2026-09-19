# Вам дан список чисел, в котором значения могут повторяться.
# Напишите функцию count_unique_values(numbers), которая возвращает количество уникальных значений в списке.

def count_unique_values(numbers):
    unique_values = len(set(numbers))
    return unique_values

print(count_unique_values([1,2,1,4,4,6,7,8,9,10]))
