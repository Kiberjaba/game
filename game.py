import numpy as np

# Инициализация игрового поля
board = np.full((3, 3), ' ')

# Функция для вывода игрового поля
def print_board():
    print("  1 2 3")
    for i, row in enumerate(board):
        print(f"{i+1} {'|'.join(row)}")
        if i < 2:
            print("  -----")

# Функция для проверки победы
def check_win(player):
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    if board[0, 0] == board[1, 1] == board[2, 2] == player or board[0, 2] == board[1, 1] == board[2, 0] == player:
        return True
    return False

# Функция для проверки ничьи
def check_draw():
    return np.all(board != ' ')

# Основной игровой цикл
player = 'X'
while True:
    print_board()
    try:
        row, col = map(int, input(f"Ход игрока {player}. Введите номер строки и столбца: ").split())
        row-=1
        col-=1
        if board[row, col] == ' ':
            board[row, col] = player
        else:
            print("Эта клетка уже занята!")
            continue
    except (ValueError, IndexError):
        print("Неверный ввод. Попробуйте снова.")
        continue

    if check_win(player):
        print_board()
        print(f"Игрок {player} победил!")
        break
    elif check_draw():
        print_board()
        print("Ничья!")
        break

    player = 'O' if player == 'X' else 'X'
