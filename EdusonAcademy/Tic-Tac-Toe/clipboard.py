def draw_board(board):
    """
    Рисует игровое поле
    """
    for i in range(3):
        print(' | '.join(board[i]))
        print('---------')

def is_integer (n):
    """
    Проверяет, введено ли число
    """
    try:
        int(n)
        return True
    except ValueError:
        return False

while True:
   X = input('Введите число: ')
   if not is_integer(X):
       print('Ошибка ввода')
       continue
   else:
       break
