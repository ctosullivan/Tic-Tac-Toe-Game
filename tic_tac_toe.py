import math

# Define variables
player = 0 # current player whose turn it is - 0-indexed - player 0 starts by default
player_selection = ["",""] # variable to keep track of which player is X and which player is O
game_over = False # variable to keep track of whether the overall program is complete or not
board = [["","",""],["","",""],["","",""]] # variable to keep track of the current board state - being a 3x3 tic tac toe board, initialised with empty strings
result = "False" # variable to hold the result of a game

# Welcome message
print("Welcome to the Tic Tac Toe game!")
print()

def order_selection() -> list:
    '''
    Function to return which player is X and which player is O. Player 0(1) gets to choose by default
    Args:
        None
    Returns:
        2x1 Array representing which player is X and which player is O 
    '''
    player_choice = False
    while not player_choice:
        player_choice = input("Player 1 choose X or O\n").upper()
        if player_choice == "X":
            print("Player 1 is X and Player 2 is O")
            return["X","O"]
        elif player_choice == "O":
            print("Player 1 is O and Player 2 is X")
            return["O","X"]
        else:
            player_choice = False

def display_board(board=list) -> None:
    '''
    Function to display the current board state
    Args:
        board - a 3x3 array representing the current board state
    Returns:
        None
    '''
    print("Current Board:")
    for i in range(0,3):
        for j in range(0,3):
            
            if board[i][j] == "":
                print((i*3)+(j)+1,end="  ")
            else:
                print(board[i][j],end="  ")    
        print()
    print()

def player_turn(player=int,player_selection=list,board=list) -> list:
    '''
    Function to take the have the current player take their turn and returning the updated board state
    Args:
        board - a 3x3 array representing the current board state
        player - int representing the current player (0 or 1)
        player_selection - 2x1 Array representing which player is X and which player is O
    Returns:
        board - a 3x3 array representing the updated board state
    '''
    player_choice = False
    while not player_choice:
        player_choice = input(f"Player {player+1} choose your move:\n")
        i = math.floor((int(player_choice)-1)/3)
        j = (int(player_choice)-1)%3
        if board[i][j] != "":
            print("Invalid position - try again.")
            player_choice = False
        else:
            board[i][j] = player_selection[player]
            return board

def check_game_over(board=list) -> any:
    '''
    Function to take the current state and check if the game over condition exists - either a win by 3 in a row, or a draw.
    Args:
        board - a 3x3 array representing the current board state
    Returns:
        str or int - returns either the winning player: 0 or 1 or "DRAW". Returns "False" if the game is not over
    '''
    # top-horizontal win condition
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] != "":
        return player_selection.index(board[0][2])
    # middle-horizontal win condition
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] != "":
        return player_selection.index(board[1][2])
    # bottom-horizontal win condition
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] != "":
        return player_selection.index(board[2][2])
    # left-vertical win condition
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] != "":
        return player_selection.index(board[2][0])
    # middle-vertical win condition
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] != "":
        return player_selection.index(board[2][1])
    # right-vertical win condition
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] != "":
        return player_selection.index(board[2][2])
    # left-diagonal win condition
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != "":
        return player_selection.index(board[2][2])
    # right-diagonal win condition
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != "":
        return player_selection.index(board[2][0])
    else:
        for i in range(0,3):
            for j in range(0,3):          
                if board[i][j] == "":
                    return "False"
        return "DRAW"
    
player_selection = order_selection()
while not game_over:
    display_board(board)
    board = player_turn(player,player_selection,board)
    result = check_game_over(board)
    if result == "False":
        # Toggle the current player
        if player == 1:
            player = 0
            continue
        else:
            player = 1
            continue
    elif result == 0:
        display_board(board)
        print("Player 1 has won the game!")
    elif result == 1:
        display_board(board)
        print("Player 2 has won the game!") 
    elif result == "DRAW": 
        print("Result is a draw!")

    play_again = False
    while not play_again:
        play_again = input("Do you want to play again - Y/N?\n").upper()
        if play_again == "Y":
            player = 0
            player_selection = ["",""]
            board = [["","",""],["","",""],["","",""]]
            result = "False"
            player_selection = order_selection()
            game_over = False
            break
        if play_again == "N":
            game_over = True
            print("BYE!")
            break