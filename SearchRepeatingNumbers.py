# Создайте функцию crosscheck(), которая принимает на вход два аргумента
# — два списка целых чисел. Функция должна найти числа,
# которые есть сразу в двух списках.
# В качестве ответа верните список этих чисел.

def crosscheck(list1, list2):
    list3 = []
    for el in list1:
        if el in list2:
            list3.append(el)
    return list3

print(crosscheck([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]))



# Альтернативное решение с помощью преобразования списков
# во множества и нахождения их пересечений

def crosscheck(numbers1, numbers2):
    result = set(numbers1).intersection(set(numbers2))
    return list(result)

print(crosscheck([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]))