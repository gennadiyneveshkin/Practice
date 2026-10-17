flag = True
while flag:
    X = input('Введите двузначное число: ')
    try:
        int(X)
        flag = False
    except ValueError:
        print('Ошибка ввода')
