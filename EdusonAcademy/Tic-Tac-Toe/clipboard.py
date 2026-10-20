def make_move (player, board)-> None:
    while True:
        coord = input(f'Введите двузначное число, координаты {player}: ')
        if not is_correct_coordinates(coord):
            print('Неверные координаты. Используйте цифры от 1 до 3')
            continue
        if is_cell_occupied(coord, board):
            print('Ячейка занята')
            continue
        break

    row, col = transform(X)

    # Ставим крестик или нолик в указанную ячейку
    board[row][col] = player

    # Отрисовываем доску после изменений
    draw_board(board)