#Генерируем двумерный список из пробелов
board = [[' ' for x in range(3)] for x in range(3)]

# Счетчик ходов
count = 0

# Продолжаем цикл пока кто-то не победит, либо не будет использовано максимальное количество ходов (9)
while True:

    X = input('Введите двузначное число - координаты крестика.\n'
            'Первая цифра - номер строки.\n'
            'Вторая цифра - номер яцейки в строке: ')
    isinteger(Х)
    continue


def draw_board(board):
    """
    Рисует игровое поле
    """
    for i in range(3):
        print(' | '.join(board[i]))
        print('---------')

# Проверяем, являются ли введенные символы числом
def isinteger (N):
    flag = True
    while flag:
        try:
            int(N)
        except ValueError:
            print('Ошибка ввода')
        continue

        # Проверяем правильность ввода
        # Если цифры введенного числа не лежат в диапазоне от 1 до 3

        if len(X) != 2:
            print('Ошибка ввода')
            continue

        if(int(X[0]) <= 0 or
            int(X[0]) > 3 or
            int(X[1])  <= 0 or
            int(X[1]) > 3
            ):
            print('Неверные координаты. Используйте цифры от 1 до 3')
            continue

        else:
            # Преобразуем число где первый элемент имеет индекс 0, т.к пользователь будет вводить координаты
            # отсчитывая от 1
            X = str(int(X[0]) - 1) + str(int(X[1]) - 1)

            # Проверяем, свободна ли ячейка
            if board [int(X[0])][int(X[1])] == 'X' or board [int(X[0])][int(X[1])] == 'O':
                print('Ячейка занята')

            else:
                # Ставим крестик в указанную ячейку
                board [int(X[0])][int(X[1])] = 'X'

                # Счетчик ходов  + 1
                count += 1

                # Выходим из цикла
                full = False

    if (all(x == 'X' for x in board[0]) or
        all(x == 'X' for x in board[1]) or
        all(x == 'X' for x in board[2])
    ):
        print('Крестики победили!')
        break

    elif (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or
          board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or
          board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'
    ):
        print('Крестики победили!')
        break

    elif (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or
          board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'
    ):
        print('Крестики победили!')
        break

    draw_board(board)

    if count >= 9:
        print('Ничья!')
        break

    full = True
    while full:

        flag = True
        while flag:
            O = input('Введите двузначное число - координаты нолика.\n'
                      'Первая цифра - номер строки.\n'
                      'Вторая цифра - номер яцейки в строке: ')
            try:
                int(O)
                flag = False
            except ValueError:
                print('Ошибка ввода')

        # Проверяем правильность ввода
        # Если цифры введенного числа не лежат в диапазоне от 1 до 3
        if (int(O[0]) <= 0 or
            int(O[0]) > 3 or
            int(O[1]) <= 0 or
            int(O[1]) > 3 or
            len(O) != 2
        ):
            print('Неверные координаты. Используйте цифры от 1 до 3')

        else:
            # Преобразуем число где первый элемент имеет индекс 0, т.к пользователь будет вводить координаты
            # отсчитывая от 1
            O = str(int(O[0]) - 1) + str(int(O[1]) - 1)

            # Проверяем, свободна ли ячейка
            if board[int(O[0])][int(O[1])] == 'X' or board[int(O[0])][int(O[1])] == 'O':
                print('Ячейка занята')

            else:
                # Ставим крестик в указанную ячейку
                board[int(O[0])][int(O[1])] = 'O'

                # Счетчик ходов  + 1
                count += 1

                # Выходим из цикла
                full = False

    if (all(x == 'O' for x in board[0]) or
            all(x == 'O' for x in board[1]) or
            all(x == 'O' for x in board[2])
    ):
        print('Нолики победили!')
        break

    elif (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or
          board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or
          board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'
    ):
        print('Нолики победили!')
        break

    elif (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or
          board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'
    ):
        print('Нолики победили!')
        break

    draw_board(board)

draw_board(board)