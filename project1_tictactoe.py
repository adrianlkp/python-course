# DISPLAY INSTRUCTIONS FOR NEW GAME
def display_instructions():
    print("Welcome to Tic-Tac-Toe")
    print("Enter number as illustrated on board to mark your 'X' or 'O'.")
    print("First player starts with 'X'") 


# DISPLAY TIC-TAC-TOE BOARD
def display_board():
    print('\n Tic-Tac-Toe\n')
    print(f'  {board_list[6]} | {board_list[7]} | {board_list[8]}')
    print('-------------')
    print(f'  {board_list[3]} | {board_list[4]} | {board_list[5]}')
    print('-------------')
    print(f'  {board_list[0]} | {board_list[1]} | {board_list[2]}\n')


# RETRIEVE PLAYER'S INPUT/POSITION TO BE MARKED
def player_input(board_list, turn_count):
    pos = ''
    accepted_range = ['1','2','3','4','5','6','7','8','9']
    accepted_value = False
    
    while accepted_value == False:
        
        # Message to player to enter input depending on turn
        if turn_count%2 != 0:
            pos = input("Player 1, enter between 1-9 to mark your 'X': ")
            mark = 'X'
        else:
            pos = input("Player 2, enter between 1-9 to mark your 'O': ")
            mark = 'O'
 
        if pos not in accepted_range:
            print('Invalid input, please enter between 1-9 only.\n')
        elif board_list[int(pos)-1] != ' ':
            print('Position already has a mark, please select an empty position.\n')
        else:
            accepted_value = True
        
    return (int(pos), mark)


# UPDATE THE BOARD LIST VALUES WITH PLAYER'S INPUT
def update_board_list(board_list, pos_mark):
    board_list[pos_mark[0]-1] = pos_mark[1] 
    return board_list


# CHECK IF THERE IS A WINNER
def check_for_win(board):
    
    if (board[0] == board[1] == board[2] != ' ') or \
       (board[3] == board[4] == board[5] != ' ') or \
       (board[6] == board[7] == board[8] != ' ') or \
       (board[0] == board[3] == board[6] != ' ') or \
       (board[1] == board[4] == board[7] != ' ') or \
       (board[2] == board[5] == board[8] != ' ') or \
       (board[0] == board[4] == board[8] != ' ') or \
       (board[6] == board[4] == board[2] != ' '):
        return 'win'
    elif ' ' not in board:
        return 'draw'
    else:
        return ''


# CHECK IF PLAYER WANTS TO RESTART OR END GAME
def restart_game():
    y_n = ''
        
    while y_n not in ['Y','N']:
        y_n = input('Do you want to restart a new game? Y or N: ')
        
        if y_n not in ['Y','N']:
            print('Invalid input, please enter Y or N.')
            
    if y_n == 'Y':
        return True
    else:
        return False


# MAIN GAME LOGIC
new_game = True
game_completed = False
turn_count = 1
board_list = []
player = ''

while game_completed == False:
    
    # Display instructions if new game, else refresh board
    if new_game == True:
        board_list = [1,2,3,4,5,6,7,8,9]
        display_instructions()
        display_board()
        
        # Clear board list after initial instructions
        board_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  
        new_game = False
    else:
        display_board()
        
    # Player enters input
    pos_mark = player_input(board_list, turn_count)
    
    # Update and refresh board
    board_list = update_board_list(board_list, pos_mark)
    
    # Check if there is a win or draw
    if check_for_win(board_list) == 'win':
        if turn_count%2 != 0:
            player = 'PLAYER 1'
        else:
            player = 'PLAYER 2'
        
        display_board()
        print(f'{player} WINS!')
        game_completed = True
    elif check_for_win(board_list) == 'draw':
        display_board()
        print('DRAW!')
        game_completed = True
    else:
        game_completed = False
            
    turn_count += 1
    
    # When game is completed, check if player wants to restart game
    if game_completed == True:
        if restart_game() == True:
            game_completed = False
            turn_count = 1
            new_game = True
        else:
            print('Thank you for playing!')
