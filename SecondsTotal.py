# Пересчет дней, часов, минут и секунд в общее к-во секунд

print('К-во дней')
days = int(input())
print('К-во часов')
hours = int(input())
print('К-во минут')
minutes = int(input())
print('К-во секунд')
seconds = int(input())


def seconds_total(days, hours, minutes, seconds):
    min_to_sec = minutes * 60
    hour_to_sec = hours * 60 ** 2
    day_to_sec = days * 60 ** 3
    return day_to_sec + hour_to_sec + min_to_sec + seconds


print(f'Всего {seconds_total(days, hours, minutes, seconds)} секунд')


# Альтернативный вариант
def seconds_total_alt(days, hours, minutes, seconds):
    return days*86400 + hours*3600 + minutes*60 + seconds
data = input('Введите временной промежуток в формате: число дней, число часов, число минут, число секунд')

#TODO Создание списка из строки разбиением по запятой!
data_list = data.split(',')

#TODO Подаем на вход функции элементы списка!
seconds_total_alt(int(data_list[0]), int(data_list[1]), int(data_list[2]), int(data_list[3]))
print(f'Всего {seconds_total(days, hours, minutes, seconds)} секунд')

print('\n')
print(data)
print(type(data))
print(data_list)
print(type(data_list))