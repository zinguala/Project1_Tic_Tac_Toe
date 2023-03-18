import random
import time


# functions:----------------------------------------------------------------------------------------


def current(*args):  # prints the current board situation with map
    for i in range((len(args))):
        for k in range(len(args[i])):
            print(*args[i][k], sep=' | ')  # print the string without to quotes ''
    print('\n')
    return None


def win_check(args):  # function for win check if player wins it returns the symbol of the winner if not return None.
    count_for_win = len(args)   # set how many symbols in a sequence for wining
    count_first_diagonal_x = 0            # declare the count for first (00,11,22,33,....) diagonal check 'x'
    count_first_diagonal_o = 0              # declare the count for first (00,11,22,33,....) diagonal check 'o'
    count_second_diagonal_x = 0              # declare the count for second diagonal (x0,..,21,12,..,0x) check 'x'
    count_second_diagonal_o = 0              # declare the count for second diagonal (x0,..,21,12,..,0x) check 'o'
    for i in range(len(args)):
        count_line_x = 0  # declare and rest the counter for x in one line
        count_line_o = 0  # declare and rest the counter for o in one line
        count_row_x = 0  # declare and rest the count for new row check 'x'
        count_row_o = 0  # declare and rest the count for new row check 'o'
        for k in range(len(args)):     # row check for win
            if args[i][k] == 'x':
                count_row_x += 1       # count 1 up when there is x in this place
                if count_row_x == count_for_win:
                    return 'x'
            elif args[i][k] == 'o':
                count_row_o += 1       # count 1 up when there is o in this place
                if count_row_o == count_for_win:          # see if the o counter in row reached to the limit for win
                    return 'o'
            if args[k][i] == 'x':       # lines check for win
                count_line_x += 1       # count 1 up when there is x in this place
                if count_line_x == count_for_win:      # see if the x counter in line reached to the limit for win
                    return 'x'
            elif args[k][i] == 'o':
                count_line_o += 1                       # count 1 up when there is o in this place
                if count_line_o == count_for_win:        # see if the o counter in line reached to the limit for win
                    return 'o'
            if i == k:     # check the first diagonal (00,11,22,33,....) for sequence in one symbol
                if args[i][k] == 'x':
                    count_first_diagonal_x += 1    # count 1 up when there is x in this place
                    if count_first_diagonal_x == count_for_win:
                        return 'x'
                elif args[i][k] == 'o':
                    count_first_diagonal_o += 1     # count 1 up when there is o in this place
                    if count_first_diagonal_o == count_for_win:
                        return 'o'

    for j in range(len(args)):                 # new for the second diagonal check
        if args[count_for_win - j - 1][j] == 'x':   # check the second diagonal (x0,..,21,12,..,0x) for sequence
            count_second_diagonal_x += 1
            if count_second_diagonal_x == count_for_win:
                return 'x'
        elif args[count_for_win - j - 1][j] == 'o':
            count_second_diagonal_o += 1
            if count_second_diagonal_o == count_for_win:
                return 'o'
    return None


# main code:---------------------------------------------------------------------------------------------
Program_Run = True   # for running while that runs the whole Program until hitting exit.
Menu = 0            # varible for a menu so the player can choose
Game_Board_size3 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
Game_map_size3 = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]
Game_board_size4 = [['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']]
Game_map_size4 = [['00', '01', '02', '03'], ['10', '11', '12', '13'], ['20', '21', '22', '23'],
                  ['30', '31', '32', '33']]
counter_for_draw = 0

while Program_Run:
    Game_Board = []
    Game_map = []
    counter_for_draw = 0
    Player = 0
    print('Welcome noughts and crosses :) \nTo Choose which game you want to play press: \n 1-player vs player\n'
          ' 2-player vs computer\n 3-computer vs computer\n 4-exit\n')
    try:
        Menu = int(input('please choose now : '))
    except ValueError:
        print('try again')
        continue

    if Menu == 1:
        print('welcome to player vs player \n')
        while True:          # while for checking the input of the size of the game board so it will be 3 or 4 only
            try:
                Board_size = int(input('please select board size 3 or 4 : '))  # player can choose the size of the board
            except ValueError:
                continue
            if Board_size == 3:
                print(f'You choose size: {Board_size}x{Board_size}\n')
                Game_Board = Game_Board_size3
                Game_map = Game_map_size3
                break
            if Board_size == 4:
                print(f'You choose size: {Board_size}x{Board_size}\n')
                Game_Board = Game_board_size4
                Game_map = Game_map_size4
                break
        current(Game_Board)
        current(Game_map)
        print('first player you choose where to place -x\nsecond player you choose where to place -o\n ')
        while True:                          # while that running the initial game
            while True:                   # while for player 1 turn
                print('Player 1 your turn, please choose where to put-x \n')
                try:
                    Row = int(input("first Enter row : "))
                except ValueError:
                    continue
                try:
                    Line = int(input("now Enter line : "))
                except ValueError:
                    continue
                if (Row not in range(len(Game_Board))) or (Line not in range(len(Game_Board))): # check coordinates if in range
                    print(f'please enter valid number between 0 - {(len(Game_Board)-1)}\n')
                elif Game_Board[Row][Line] != '_':                            # check if this square is already taken
                    print(f'this square {Row}{Line} is already taken please choose other one')
                else:
                    Game_Board[Row][Line] = 'x'            # insert the symbol of the player in the coordinates chose
                    counter_for_draw += 1
                    break
            current(Game_Board)                     # calls the current function to show the board
            current(Game_map)                        # calls the current function to show the map
            if win_check(Game_Board) == 'x':          # winner check with win_check function
                print('player 1 you are the winner!!!!!!!!!!!!!!!\n')
                break
            if counter_for_draw == (len(Game_Board) ** 2):        # draw check if now squares left
                print('Its a Draw no one wins :)\n')
                break
            print('Player 2 your turn, please choose where to put-o \n')
            while True:                       # while for turn of player 2
                try:
                    Row = int(input("first Enter row : "))        # coordinates choose
                except ValueError:
                    continue
                try:
                    Line = int(input("now Enter line : "))        # coordinates choose
                except ValueError:
                    continue
                if (Row not in range(len(Game_Board))) or (Line not in range(len(Game_Board))): # check coordinates if in range
                    print(f'please enter valid number between 0 - {(len(Game_Board)-1)}\n')
                elif Game_Board[Row][Line] != '_':                            # check if this square is already taken
                    print(f'this square {Row}{Line} is already taken please choose other one')
                else:
                    Game_Board[Row][Line] = 'o'        # insert the symbol of the player in the coordinates chose
                    counter_for_draw += 1
                    break
            current(Game_Board)                       # calls the current function to show the board
            current(Game_map)                         # calls the current function to show the map
            if win_check(Game_Board) == 'o':         # winner check with win_check function
                print('player 2 you are the winner!!!!!!!!!!!!!!!\n')
                break
            if counter_for_draw == (len(Game_Board) ** 2):
                print('Its a Draw no one wins :)\n')
                break
    elif Menu == 2:
        print('welcome to player vs computer \n')
        while True:  # while for checking the input of the size of the game board so it will be 3 or 4 only
            try:
                Board_size = int(input('please select board size 3 or 4 : '))  # player can choose the size of the board
            except ValueError:
                continue
            if Board_size == 3:
                print(f'You choose size: {Board_size}x{Board_size}\n')
                Game_Board = Game_Board_size3
                Game_map = Game_map_size3
                break
            if Board_size == 4:
                print(f'You choose size: {Board_size}x{Board_size}\n')
                Game_Board = Game_board_size4
                Game_map = Game_map_size4
                break
        while True:
            try:
                Player = int(input('please choose first player (place x) or second player (place o) : '))
            except ValueError:
                print('please insert choose 1 or 2 \n')
                continue
            if Player == 1 or Player == 2:
                break

        current(Game_Board)
        current(Game_map)
        if Player == 1:
            while True:  # while that running the initial game
                print('Player 1 your turn, please choose where to put-x \n')
                while True:  # while for player 1 turn
                    try:
                        Row = int(input("first Enter row : "))
                    except ValueError:
                        continue
                    try:
                        Line = int(input("now Enter line : "))
                    except ValueError:
                        continue
                    if (Row not in range(len(Game_Board))) or (
                            Line not in range(len(Game_Board))):  # check coordinates if in range
                        print(f'please enter valid number between 0 - {(len(Game_Board) - 1)}\n')
                    elif Game_Board[Row][Line] != '_':  # check if this square is already taken
                        print(f'this square {Row}{Line} is already taken please choose other one')
                    else:
                        Game_Board[Row][Line] = 'x'  # insert the symbol of the player in the coordinates chose
                        counter_for_draw += 1
                        break
                current(Game_Board)  # calls the current function to show the board
                current(Game_map)  # calls the current function to show the map
                if win_check(Game_Board) == 'x':  # winner check with win_check function
                    print('player 1 you are the winner!!!!!!!!!!!!!!!\n')
                    break
                if counter_for_draw == (len(Game_Board) ** 2):
                    print('Its a Draw no one wins :)')
                    break
                print('now its the computer turn  \n')
                while True:  # while for turn of player 2
                    Row = random.randrange(0, len(Game_Board))  # coordinates choose
                    Line = random.randrange(0, len(Game_Board))  # coordinates choose
                    if Game_Board[Row][Line] == '_':  # check if this square is already taken
                        Game_Board[Row][Line] = 'o'  # insert the symbol of the player in the coordinates chose
                        counter_for_draw += 1
                        break

                current(Game_Board)  # calls the current function to show the board
                current(Game_map)  # calls the current function to show the map
                if win_check(Game_Board) == 'o':  # winner check with win_check function
                    print('player 2 you are the winner!!!!!!!!!!!!!!!\n')
                    break

                if counter_for_draw == (len(Game_Board)**2):
                    print('Its a Draw no one wins :)\n')
                    break
        elif Player == 2:
            while True:  # while that running the initial game
                print('now its the computer turn  \n')
                while True:  # while for turn of player 1
                    Row = random.randrange(0, len(Game_Board))  # coordinates choose
                    Line = random.randrange(0, len(Game_Board))  # coordinates choose
                    if Game_Board[Row][Line] == '_':  # check if this square is already taken
                        Game_Board[Row][Line] = 'x'  # insert the symbol of the player in the coordinates chose
                        counter_for_draw += 1
                        break
                current(Game_Board)  # calls the current function to show the board
                current(Game_map)  # calls the current function to show the map
                if win_check(Game_Board) == 'x':  # winner check with win_check function
                    print('computer wins !!!!!!!!!!!!!!!\n')
                    break

                if counter_for_draw == (len(Game_Board) ** 2):
                    print('Its a Draw no one wins :)')
                    break
                while True:  # while for player 1 turn
                    print('Player 2 your turn, please choose where to put-o \n')
                    try:
                        Row = int(input("first Enter row : "))
                    except ValueError:
                        continue
                    try:
                        Line = int(input("now Enter line : "))
                    except ValueError:
                        continue
                    if (Row not in range(len(Game_Board))) or (
                            Line not in range(len(Game_Board))):  # check coordinates if in range
                        print(f'please enter valid number between 0 - {(len(Game_Board) - 1)}\n')
                    elif Game_Board[Row][Line] != '_':  # check if this square is already taken
                        print(f'this square {Row}{Line} is already taken please choose other one')
                    else:
                        Game_Board[Row][Line] = 'o'  # insert the symbol of the player in the coordinates chose
                        counter_for_draw += 1
                        break
                current(Game_Board)  # calls the current function to show the board
                current(Game_map)  # calls the current function to show the map
                if win_check(Game_Board) == 'o':  # winner check with win_check function
                    print('player 2 you are the winner!!!!!!!!!!!!!!!\n')
                    break
                if counter_for_draw == (len(Game_Board) ** 2):
                    print('Its a Draw no one wins :)')
                    break
    elif Menu == 3:
        print('welcome to computer vs computer \n')
        while True:  # while for checking the input of the size of the game board so it will be 3 or 4 only
            try:
                Board_size = int(input('please select board size 3 or 4 : '))  # player can choose the size of the board
            except ValueError:
                continue
            if Board_size == 3:
                print(f'You choose size: {Board_size}x{Board_size}\n')
                Game_Board = Game_Board_size3
                Game_map = Game_map_size3
                break
            if Board_size == 4:
                print(f'You choose size: {Board_size}x{Board_size}\n')
                Game_Board = Game_board_size4
                Game_map = Game_map_size4
                break
        while True:  # while that running the initial game
            print('now its the computer 1 turn  \n')
            while True:  # while for turn of player 1
                Row = random.randrange(0, len(Game_Board))  # coordinates choose
                Line = random.randrange(0, len(Game_Board))  # coordinates choose
                if Game_Board[Row][Line] == '_':  # check if this square is already taken
                    Game_Board[Row][Line] = 'x'  # insert the symbol of the player in the coordinates chose
                    counter_for_draw += 1
                    break
            current(Game_Board)  # calls the current function to show the board
            current(Game_map)  # calls the current function to show the map
            if win_check(Game_Board) == 'x':  # winner check with win_check function
                print('computer 1 is the winner !!!!!!!!!!!!!!!\n')
                break
            if counter_for_draw == (len(Game_Board) ** 2):
                print('Its a Draw no one wins :)')
                break
            time.sleep(3)
            print('now its the computer 2 turn  \n')
            while True:  # while for turn of player 1
                Row = random.randrange(0, len(Game_Board))  # coordinates choose
                Line = random.randrange(0, len(Game_Board))  # coordinates choose
                if Game_Board[Row][Line] == '_':  # check if this square is already taken
                    Game_Board[Row][Line] = 'o'  # insert the symbol of the player in the coordinates chose
                    counter_for_draw += 1
                    break
            current(Game_Board)  # calls the current function to show the board
            current(Game_map)  # calls the current function to show the map
            if win_check(Game_Board) == 'o':  # winner check with win_check function
                print('computer 2 is the winner!!!!!!!!!!!!!!!\n')
                break
            if counter_for_draw == (len(Game_Board) ** 2):
                print('Its a Draw no one wins :)')
                break
            time.sleep(3)
    elif Menu == 4:
        print('Goodbye')
        Program_Run = False







