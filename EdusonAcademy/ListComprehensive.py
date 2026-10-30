# Напишите функцию flatten_tuple, которая принимает на вход кортеж tup,
# содержащий внутри себя другие кортежи (подсписки). Функция должна вернуть список,
# состоящий из всех элементов подсписков.

def flatten_tuple (tup):
    return [x for el in tup for x in el]

tup1 = ((1, 2), (), (3, 4, 5))
print(flatten_tuple(tup1))

# Напишите функцию sum_positive_numbers, которая принимает список целых чисел numbers и возвращает сумму
# только положительных чисел из данного списка.

# Решение с помощью генератора списков
def sum_positive_numbers (numbers):
    lst = [x for x in numbers if x > 0]
    return sum(lst)


# Решение с помощью герератора, без формирования допольнительного списка
def sum_positive_numbers2 (numbers):
    return sum (x for x in numbers if x > 0)

# Напишите функцию process_array, которая принимает список целых чисел numbers и возвращает новый список,
# содержащий только положительные числа, умноженные на 2.

def process_array (numbers):
    return [x*2 for x in numbers if x > 0]


# Напишите функцию list_to_dict, которая принимает список ключей и список значений.
# А затем возвращает словарь, сформированный из этих списков.
# Используйте генератор списка и специальную функцию.

def list_to_dict (k, v):
    return {x : y for x, y in zip (k, v)}



def sum_n_dimensional_vectors (vectors):
    return sum (el for vector in vectors for el in vector)

print (sum_n_dimensional_vectors ([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# Список сумм внутренних списков
vects = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = [sum (vect) for vect in vects]

print(lst)

# Найти максимальное значение в списке, которое не превышает значение limit
def lim_max(nums, limit):

    # Идем по списку, если элемент < limit отправляем его в функцию max,
    # max принимает эти элементы, сравнивает между собой и возвращает максимальный из них
    # Если все они больше limit, возвращаем -1
    return max ((x for x in nums if x < limit), default = -1)


# Напишите функцию list_reorder, которая принимает на вход список списков list_of_lists.
# Функция должна изменить структуру списка, так чтобы элементы из вложенных списков
# стали элементами одного общего списка.

def list_reorder (list_of_lists):
    return [x for el in list_of_lists for x in el ]

