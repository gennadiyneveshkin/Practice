# Подсчет суммы цифр четырехзначного числа

def sum (a):
    sum_numbers = int(a[0]) + int(a[1]) + int(a[2]) + int(a[3])
    return sum_numbers
a = input('Введите четырехзначное число')
print(f'Сумма цифр числа {a} равна {sum (a)}')