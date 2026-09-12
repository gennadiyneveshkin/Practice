# Создайте функцию search_day(), которая посчитает количество туманных дней в списке. Она принимает в качестве аргумента список с предположительной влажностью воздуха на ближайшие пять дней. Например, такой: 76, 89, 91, 32, 10. Если влажность превышает 80%, день считается туманным. Верните список с порядковыми номерами туманных дней. Номера дней считайте с нуля.

result = []

def search_day(days):
    for el in days:
        if el > 80:
            result.append(days.index(el))
    return result

days = [76, 89, 91, 32, 10]

print(search_day(days))


result2 = []

def search_day2(days):
    for i, el in enumerate (days):
        if el > 80:
            result2.append(i)
    return result2

days = [76, 89, 91, 32, 10]

print(search_day2(days))

result3 = []
def search_day3(days):
    for i in range (len(days)):
        if days[i] > 80:
            result3.append(i)
    return result

days = [76, 89, 91, 32, 10]

print (search_day3(days))


# Этот вариант не работает
days = [76, 89, 91, 32, 10]

for el in (days):
    if el > 80:
        days.remove(el)

print(days)

# Работает, но получаем список из элементов >= 80
# А как получить список из индексов этих элементов в начальном списке days?
days = [77, 89, 91, 32, 10]
max_value = 80
result_days = [x for x in days if x >= max_value]

print(result_days)