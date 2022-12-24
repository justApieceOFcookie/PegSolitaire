

def print_board(board):
    # 打印棋盘的上边界
    print("  1 2 3 4 5 6 7")
    print("     +-+-+-+")
    for i in range(7):
        # 打印棋盘的左边界
        print(chr(ord('A') + i), end="")
        if 66 < (ord('A') + i) < 70 :
            print("|", end="")
            for j in range(7):
                if board[i][j] == 0:
                    # 打印空格
                    print(" ", end="")
                elif board[i][j] == 1:
                    # 打印棋子
                    print("O", end="")
                print("|", end="")
            print()
            print(" +-+-+-+-+-+-+-+")
        else :
            print("    |", end="")
            for j in [2,3,4]:
                if board[i][j] == 0:
                    # 打印空格
                    print(" ", end="")
                elif board[i][j] == 1:
                    # 打印棋子
                    print("O", end="")
                print("|", end="")
            print()
            print("     +-+-+-+")


def get_move(board):
    # 提示玩家输入移动的棋子的位置
    while True:
        move = input("请选择您想移动的棋子：(例如：B4)")
        if len(move) != 2:
            print("Invalid input. Please try again.")
            continue
        x = ord(move[0]) - ord('A')
        y = ord(move[1]) - ord('1')
        if x < 0 or x > 6 or y < 0 or y > 6:
            print("Invalid input. Please try again.")
            continue
        if board[x][y] != 1:
            print("You do not have a piece at this position. Please try again.")
            continue
        break
    # 提示玩家输入目标位置
    while True:
        move = input("请选择您想跳至的目标点：(例如：D4)")
        if len(move) != 2:
            print("Invalid input. Please try again.")
            continue
        x_new = ord(move[0]) - ord('A')
        y_new = ord(move[1]) - ord('1')
        if (abs(x_new - x) != 2) and (abs(y_new - y) != 2):
            print("Invalid input. Please try again.")
            continue
        if board[x_new][y_new] != 0:
            print("This position is already occupied. Please try again.")
            continue
        # 移动棋子到新位置
        board[x_new][y_new] = 1
        board[x][y] = 0
        # 去掉被跳过的棋子
        if x_new == x :
            board[x][int((y_new + y) / 2)] = 0
        else :
            board[int((x+x_new)/2)][y] = 0
        # 退出循环
        break


def game_won(board):
    # 检查是否通关
    result = 0
    for i in board:
        for j in i:
            result += j
    if result == 1 :
        return True
    return False


def play_game():
    # 初始化棋盘
    board = [[0, 0, 1, 1, 1, 0, 0],
             [0, 0, 1, 1, 1, 0, 0],
             [1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 0, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 1],
             [0, 0, 1, 1, 1, 0, 0],
             [0, 0, 1, 1, 1, 0, 0]]
    # 打印初始棋盘
    print_board(board)
    # 循环直到游戏结束
    while True:
        # 处理玩家输入并移动棋子
        get_move(board)
        # 打印新的棋盘
        print_board(board)
        # 检查游戏是否已结束
        if game_won(board):
            print("真厉害，你通关了孔明棋！")
            break

play_game()