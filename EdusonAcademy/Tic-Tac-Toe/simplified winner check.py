def is_winner(player: str, board: list) -> bool:
    # Горизонтали
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Вертикали
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Диагонали
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_winner(player: str, board: list) -> bool:
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    return False

def is_winner(player:str, board:list):
    for col in range(3):
        if all(x[col] == player for x in board):
            return True
    return False