def draw_board(board):
    """
    Рисует игровое поле
    """
    for i in range(3):
        print(' | '.join(board[i]))
        print('---------')

def is_two_digit (n:str) -> bool:
    """
    Проверяет, введено ли число и двузначное ли оно
    """
    return n.isdigit() and len(n) == 2

def is_correct_coordinates (n:str) -> bool:
    """
    Проверяет, введены ли допустимые координаты (цифры 1, 2 или 3)
    """
    k = int(n[0])
    m = int(n[1])

    return 0 < k <= 3 and 0 < m <= 3

def transform(n):

    """ Преобразуем строку с числом в формат где первый элемент имеет индекс 0
    т. к. пользователь будет вводить координаты отсчитывая от 1
    """
    n = str(int(n[0]) - 1) + str(int(n[1]) - 1)
    return n

def is_cell_occupied (n:str, board:list)->bool:
    """
    Проверяет, свободна ли ячейка
    """
    n = transform(n)
    if board[int(n[0])][int(n[1])] == 'X' or board[int(n[0])][int(n[1])] == 'O':
        return True
    return False

def is_winner(n:str, board:list):
    """
    Проверяет, является ли ход победным
    """

    # Проверка горизонталей
    for row in board:
        if all(cell == 'X' for cell in row):
            return True

    # Проверка вертикалей
    for i in range(3):

        # Если все i-е элементы
        return all(x[i] == 'X' for x in board)


    return False


# Генерируем двумерный список из пробелов
board = [[' ' for x in range(3)] for x in range(3)]

# Счетчик ходов
count = 0

while True:

    # Ход крестиков
    while True:
        X = input('Введите двузначное число, координаты крестика: ')
        if not is_two_digit(X):
            print('Ошибка ввода: Используйте цифры от 1 до 3')
            continue
        elif not is_correct_coordinates (X):
            print('Неверные координаты. Используйте цифры от 1 до 3')
            continue
        elif is_cell_occupied(X, board):
            print('Ячейка занята')
        else:
           break

    X = transform(X)

    # Ставим крестик в указанную ячейку
    # board [индекс списка][индекс элемента в этом списке]
    board [int(X[0])][int(X[1])] = 'X'

    draw_board(board)

    if is_winner('X', board):
        print ('Крестики победили!')
        break

    count += 1

    if count >= 9:
        print('Ничья!')
        break

    # Ход ноликов
    while True:
        O = input('Введите двузначное число, координаты нолика: ')
        if not is_two_digit(O):
            print('Ошибка ввода: Используйте цифры от 1 до 3')
            continue
        elif not is_correct_coordinates(O):
            print('Неверные координаты. Используйте цифры от 1 до 3')
            continue
        elif is_cell_occupied(O, board):
            print('Ячейка занята')
        else:
            break

    O = transform(O)

    # Ставим нолик в указанную ячейку
    board[int(O[0])][int(O[1])] = 'O'

    draw_board(board)

    if is_winner('O', board):
        print('Нолики победили!')
        break

    count += 1