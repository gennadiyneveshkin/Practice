def draw_board(board):
    """
    Рисует игровое поле
    """
    for i in range(3):
        print(' | '.join(board[i]))
        print('---------')

def is_correct_coordinates (n:str) -> bool:
    """
    Проверяет ввод
    """
    # Сначала проверяем формат: только цифры и ровно 2 символа
    if not isinstance(n, str) or not (n.isdigit() and len(n) == 2):
        return False

    # Теперь безопасно преобразуем в числа
    k = int(n[0])
    m = int(n[1])

    # Проверяем, что цифры в диапазоне 1–3
    return 1 <= k <= 3 and 1 <= m <= 3

def transform(n:str) -> tuple[int, int]:

    """ Преобразуем строку с числом в формат где первый элемент имеет индекс 0
    т. к. пользователь будет вводить координаты отсчитывая от 1
    """

    # Возвращаем кортеж из координат
    return int(n[0]) - 1, int(n[1]) - 1

def make_move(player, board) -> None:
    while True:
        coord = input(f'Введите двузначное число, координаты {player}: ')

        if not is_correct_coordinates(coord):
            print('Неверные координаты. Используйте цифры от 1 до 3')
            continue

        # Один раз преобразуем в индексы
        row, col = transform(coord)

        # Проверяем занятость, используя уже готовые индексы
        cell = board[row][col]
        if cell == 'X' or cell == 'O':
            print('Ячейка занята')
            continue

        break

    # Ставим крестик или нолик
    board[row][col] = player

    # Отрисовываем доску
    draw_board(board)



def is_winner(player:str, board:list) -> bool:
    """
    Проверяет, является ли ход победным
    """

    # Горизонтали
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Вертикали
    for i in range(3):
        if all(row[i] == player for row in board):
            return True

    # Диагонали
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board: list) -> bool:
    """Проверяет, заполнено ли поле (нет свободных ячеек). Если True то ничья"""
    for row in board:
        if ' ' in row:
            return False
    return True

# ------- Основная игра --------

# Генерируем двумерный список из пробелов
board = [[' ' for x in range(3)] for x in range(3)]

while True:

    # Ход крестиков
    make_move('X', board)

    if is_winner('X', board):
        print ('Крестики победили!')
        break

    if is_board_full(board):
        print('Ничья')
        break

    # Ход ноликов
    make_move('O', board)

    if is_winner('O', board):
        print('Нолики победили!')
        break

    if is_board_full(board):
        print('Ничья')
        break