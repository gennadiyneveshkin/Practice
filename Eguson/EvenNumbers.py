# Найти четные числа в заданном диапазоне

def even_numbers(start, stop):
    even_numbers = []
    for i in range (start, stop + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

print(even_numbers(3, 15))