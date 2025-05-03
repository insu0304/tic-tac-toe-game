import random

board = ['' for _ in range(9)]

def print_board():
    row1 = '  {}  | {}  | {} '.format(board[0],board[1],board[2])
    row2 = '  {}  | {}  | {} '.format(board[3],board[4],board[5])
    row3 = '  {}  | {}  | {} '.format(board[6],board[7],board[8])

    print()
    print(row1)
    print(f" - - - - - -  ")
    print(row2)
    print(f" - - - - - -  ")
    print(row3)


def check_win():



    win_condition=[
        
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]
    for condition in win_condition:
        if board[condition[0]]==board[condition[1]]==board[condition[2]]!='':
            return True
    return False


#if you want to done by the something thaat will definately buy

def reset_game():
    global board
    board = ['' for _ in range(9)]


def check_draw():
    return '' not in board


#a = print_board()
def ai_move():
    best_score = float('-inf')
    best_move = None
    for i in range(len(board)):
        if board[i] == '':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        board[best_move] = 'O'

def minimax(board, depth, is_maximizing):
        if check_win():
            return -10 + depth if is_maximizing else 10 - depth

        elif check_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(len(board)):
                if board[i] == '':
                    board[i] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i] = ''
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(len(board)):
                if board[i] == '':
                    board[i] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i] = ''
                    best_score = min(score, best_score)
            return best_score





def play_game():
    print("Welcome to the Tic Tac Toe Game")
    current_player = 'X'

    while True:
        print_board()
        move = input(f"Player {current_player}, enter your move (1-9) or 'r' to reset: ")
        
        if move.lower() == 'r':
            reset_game()
            current_player = 'X'
        elif move.isdigit() and 1 <= int(move) <=9:
            if board[int(move) - 1] == '':
                board[int(move) - 1] = current_player
            
                if check_win():
                        print_board()
                        print(f"Player {current_player} wins! Congratulations!")
                        if input("Play again? (y/n): ").lower() == 'y':
                            reset_game()
                            current_player = 'X'
                        else:
                            break
                
                if check_draw():
                        print_board()
                        print("It's a draw!")
                        if input("Play again? (y/n): ").lower() == 'y':
                            reset_game()
                            current_player = 'X'
                        else:
                            break

                # Switch to AI
                current_player = 'O'
                ai_move()
                
                if check_win():
                    print_board()
                    print("Player O wins! Congratulations!")
                    if input("Play again? (y/n): ").lower() == 'y':
                        reset_game()
                        current_player = 'X'
                    else:
                        break
                
                if check_draw():
                    print_board()
                    print("It's a draw!")
                    if input("Play again? (y/n): ").lower() == 'y':
                        reset_game()
                        current_player = 'X'
                    else:
                        break
                
                # Switch back to Player X
                current_player = 'X'

                
            else:
                print("Invalid move, try again.")
        else:
            print("Invalid input, try again.")

play_game()


