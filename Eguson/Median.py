
print('Введите первое число')
a = input()
print('Введите второе число')
b = input()
print('Введите второе число')
c = input()

def median(a, b, c):
    m_list = [a, b, c]
    m_list.sort()
    print(m_list)
    return m_list[1]
# переменной median присваиваем значение функции median(a, b, c)
# другими слованми: принимаем значение ф-ии median(a, b, c) в переменную median
median = median(a, b, c)
print(f'Медиана равняется {median}')