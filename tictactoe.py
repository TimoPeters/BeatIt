# Tic Tac Toe - Game

two_players = True

# 0 := empty
# 1 := X
# 2 := O
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


def game_over(board) -> bool:
    # Check horizontal
    if board[0] == board[1] and board[0] == board[2]:
        if board[0] != 0:
            return True
    elif board[3] == board[4] and board[3] == board[5]:
        if board[3] != 0:
            return True
    elif board[6] == board[7] and board[6] == board[8]:
        if board[6] != 0:
            return True

    # Check vertical
    if board[0] == board[3] and board[0] == board[6]:
        if board[0] != 0:
            return True
    elif board[1] == board[4] and board[1] == board[7]:
        if board[1] != 0:
            return True
    elif board[2] == board[5] and board[2] == board[8]:
        if board[2] != 0:
            return True

    # Check diagonal
    if board[0] == board[4] and board[0] == board[8]:
        if board[0] != 0:
            return True
    elif board[2] == board[4] and board[2] == board[6]:
        if board[2] != 0:
            return True

    return False


def clean_board(board):
    board[0] = 0
    board[1] = 0
    board[2] = 0
    board[3] = 0
    board[4] = 0
    board[5] = 0
    board[6] = 0
    board[7] = 0
    board[8] = 0


def play_again():
    while True:
        play_again_input = input("Do you want to play again? (yes/no): ")
        if play_again_input == "yes":
            return True
        elif play_again_input == "no":
            return False
        else:
            print_board("Type 'yes' or 'no'")


def print_board(board):
    str_board = []
    print("----------------------------------------------")
    for i in board:
        if i == 0:
            str_board.append("   ")
        elif i == 1:
            str_board.append(" X ")
        else:
            str_board.append(" O ")

    print(str_board[0] + "|" + str_board[1] + "|" + str_board[2])
    print("- - - - - - ")
    print(str_board[3] + "|" + str_board[4] + "|" + str_board[5])
    print("- - - - - - ")
    print(str_board[6] + "|" + str_board[7] + "|" + str_board[8])


def run_game(board):
    print_board(board)
    print("X begins")

    correct_input = False
    player = 1
    player_str = "X"
    player_input = input(player_str + ": ")
    board[int(player_input) - 1] = player

    while True:
        if player == 1:
            player = 2
            player_str = "O"
        else:
            player = 1
            player_str = "X"

        print_board(board)
        while not correct_input:
            player_input = input(player_str + ": ")
            if (0 < int(player_input) < 10) and (board[int(player_input) - 1] == 0):
                correct_input = True
                board[int(player_input) - 1] = player
        correct_input = False
        if game_over(board):
            print_board(board)
            print(player_str + " wins")
            if play_again():
                clean_board(board)
                player = 2
            else:
                break
        elif not board.__contains__(0):
            print_board(board)
            print("Draw")
            if play_again():
                clean_board(board)
                player = 2
            else:
                break


run_game(board)
