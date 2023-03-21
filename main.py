import random  # used for the computer for random coordinates
import time  # used for timer when computer vs computer so the game will run at a slower pace


# functions:----------------------------------------------------------------------------------------

def current(args):  # prints the current board situation with map
    middle_lines = 0  # count the separate rows lines 'so' they will be in the middle of the board
    for c in args:  # for to start printing
        between_lines = 0  # counter for between the lines separations
        if len(args[0][0]) == 1:  # if for placing the print in the center
            print('            ', end='')  # if printing 1 str print more spaces

        else:  # if printing 2 str print 1 less space
            print('           ', end='')

        for r in c:  # now printing every word ending with no space
            print(r, end='')  # print the string

            between_lines += 1  # count up lines

            if between_lines != (len(args)):  # print lines between lines (' | ') with no space
                print(' | ', end='')
            else:
                print('')  # if last line do not print lines (' | ')!

        middle_lines += 1

        if middle_lines != (len(args)):  # if not last row printing rows lines ('------')
            if len(args[0][0]) == 1:  # if contain 1 str print more spaces
                print('           ', end='')
                for q in range(len(args) - 1):  # for to print long line as the length of the matrix
                    print('---+', end='')
                print('---')
            elif len(args[0][0]) == 2:  # if contain 2 str print less spaces
                print('          ', end='')
                for w in range(len(args) - 1):  # for to print long line as the length of the matrix
                    print('----+', end='')
                print('----')
    print('\n')
    return None


def win_check(args, player_help=0):  # function for win check and option to help the player.
    count_for_win = len(args)  # set how many symbols in a sequence for wining
    count_first_diagonal_x = 0  # declare the count for first (00,11,22,33,....) diagonal check 'x'
    count_first_diagonal_o = 0  # declare the count for first (00,11,22,33,....) diagonal check 'o'
    count_second_diagonal_x = 0  # declare the count for second diagonal (x0,..,21,12,..,0x) check 'x'
    count_second_diagonal_o = 0  # declare the count for second diagonal (x0,..,21,12,..,0x) check 'o'
    for i in range(len(args)):
        count_line_x = 0  # declare and rest the counter for x in one line
        count_line_o = 0  # declare and rest the counter for o in one line
        count_row_x = 0  # declare and rest the count for new row check 'x'
        count_row_o = 0  # declare and rest the count for new row check 'o'
        for k in range(len(args)):

            if args[i][k] == 'x':  # row check for win player 1
                count_row_x += 1  # count 1 up when there is x in this place
                if count_row_x == count_for_win:  # check for win in row
                    return 'x'
                if player_help == 1 and count_row_x == (count_for_win - 1):  # help for player 1 for row win next move
                    try:  # added this to ignore the error if there isn't '_' in this row.
                        print(f'Player 1 next move for win choose square: {i}', args[i].index('_'), sep='')
                    except ValueError:  # if there is error print nothing
                        print('')

            elif args[i][k] == 'o':  # row check for win player 2
                count_row_o += 1  # count 1 up when there is o in this place
                if count_row_o == count_for_win:  # see if the o counter in row reached to the limit for win
                    return 'o'
                if player_help == 2 and count_row_o == (count_for_win - 1):  # help for player 2 for row win next move
                    try:  # added this to ignore the error if there isn't '_' in this row.
                        print(f'Player 2 next move for win choose square: {i}', args[i].index('_'), sep='')
                    except ValueError:  # if there is error print nothing
                        print('')

            if args[k][i] == 'x':  # lines check for win player 1
                count_line_x += 1  # count 1 up when there is x in this place
                if count_line_x == count_for_win:  # see if the x counter in line reached to the limit for win
                    return 'x'
                if player_help == 1 and count_line_x == (count_for_win - 1):  # help for player 1 for line win next move
                    for r in range(len(args)):  # for to find where is the only '_' that left
                        if args[r][i] == '_':
                            print(f'Player 1 next move for win choose square: {r}{i}')

            elif args[k][i] == 'o':
                count_line_o += 1  # count 1 up when there is o in this place
                if count_line_o == count_for_win:  # see if the o counter in line reached to the limit for win
                    return 'o'
                if player_help == 2 and count_line_o == (count_for_win - 1):  # help for player 2 for line win next move
                    for j in range(len(args)):  # for to find where is the only '_' that left
                        if args[j][i] == '_':
                            print(f'Player 2 next move for win choose square: {j}{i}')

            if i == k:  # check the first diagonal (00,11,22,33,....) for sequence in one symbol
                if args[i][k] == 'x':
                    count_first_diagonal_x += 1  # count 1 up when there is x in this place
                    if count_first_diagonal_x == count_for_win:  # see if the x counter reached to the limit for win
                        return 'x'
                elif args[i][k] == 'o':
                    count_first_diagonal_o += 1  # count 1 up when there is o in this place
                    if count_first_diagonal_o == count_for_win:  # see if the o counter reached to the limit for win
                        return 'o'

    if player_help == 1 and count_first_diagonal_x == (count_for_win - 1):  # help for player 1 first diagonal
        for v in range(count_for_win):
            if args[v][v] == '_':  # for to find where is the only '_' that left
                print(f'Player 1 next move for win choose square: {v}{v}')

    if player_help == 2 and count_first_diagonal_o == (count_for_win - 1):  # help for player 2 diagonal
        for u in range(count_for_win):  # for to find where is the only '_' that left
            if args[u][u] == '_':
                print(f'Player 2 next move for win choose square: {u}{u}')

    for j in range(len(args)):  # check the second diagonal (x0,...,21,12,...,0x) for sequence
        if args[count_for_win - j - 1][j] == 'x':
            count_second_diagonal_x += 1  # count 1 up when there is x in this place
            if count_second_diagonal_x == count_for_win:  # see if the x counter reached to the limit for win
                return 'x'

        elif args[count_for_win - j - 1][j] == 'o':
            count_second_diagonal_o += 1  # count 1 up when there is o in this place
            if count_second_diagonal_o == count_for_win:  # see if the x counter reached to the limit for win
                return 'o'

    if player_help == 1 and count_second_diagonal_x == (count_for_win - 1):  # help for player 1 second diagonal
        for r in range(len(args)):  # second diagonal check for the
            if args[count_for_win - r - 1][r] == '_':  # check the second diagonal for the last '_' coordinates
                print(f'Player 2 next move for win choose square: {count_for_win - r - 1}{r}')

    if player_help == 2 and count_second_diagonal_o == (count_for_win - 1):  # help for player 2 second diagonal
        for n in range(len(args)):  # check the second diagonal for the last '_' coordinates
            if args[count_for_win - n - 1][n] == '_':
                print(f'Player 2 next move for win choose square: {count_for_win - n - 1}{n}')

    return None


# main code:-------------------------------------------------------------------------------------
Program_Run = True  # for running while that runs the whole Program until hitting exit.
Menu = 0  # variable for a menu so the player can choose
counter_for_draw = 0
Game_Board = []
Game_map = []
board_size = 0

while Program_Run:  # while that runs the whole program

    print('Welcome noughts and crosses :)\n \nTo Choose which game you want to play press: \n 1-player vs player\n'
          ' 2-player vs computer\n 3-computer vs computer\n 4-exit\n')
    try:
        Menu = int(input('please choose now : '))  # input for choosing from the menu
    except ValueError:  # except for error or mistakes in the input for try again
        print('try again\n')
        continue

    if Menu == 1:  # if for menu choose number 1 - player vs player
        while True:  # while that runs the player vs player game
            player1_help = ''  # declare and reset help variable for player 1
            player2_help = ''  # declare and reset help variable for player 2
            Player = 0  # reset the variable that for choosing which player when player vs computer
            replay = ''  # reset the choice  if to replay the match
            cord = ''  # declare and reset cord help variable for showing coordinates on the help map
            board_size = 0
            Game_Board = []
            Game_map = []

            counter_for_draw = 0  # reset draw counter
            print('welcome to player vs player \n')

            while True:  # while for input help player 1.
                player1_help = input('Player 1 Do you want help during the game? y/n : ')
                if player1_help in ['y', 'n']:
                    print(f'user typed {player1_help}')
                    break
                else:
                    print('Type y or n')
                    continue

            while True:  # while for input help player 2
                player2_help = input('Player 2 Do you want help during the game? y/n : ')
                if player2_help in ['y', 'n']:
                    print(f'user typed {player1_help}')
                    break
                else:
                    print('Type y or n')
                    continue

            while True:  # while for checking the input of the size of the game board, so it will be 3-9 only

                try:
                    Board_size = int(input('please select board size from 3 to 9 : '))  # player choose  size of board
                except ValueError:
                    continue
                if 2 < Board_size < 10:  # check if the input within the range of 3-9
                    for x in range(Board_size):  # if yes, for in for to construct the game board
                        help_list = []
                        for b in range(Board_size):  # for this I am using two lists and append them
                            help_list.append('_')
                        Game_Board.append(help_list)

                    for o in range(Board_size):  # now I will construct the map of game board
                        help_list = []
                        for p in range(Board_size):  # using again two for loops, and two lists
                            cord = '{}{}'.format(o, p)
                            help_list.append(cord)
                        Game_map.append(help_list)

                    if Board_size == len(Game_Board):  # if all ok move break the while of board creation
                        print('\n')
                        break
                else:
                    print('please try again')
            current(Game_Board)  # prints  the game board
            current(Game_map)  # prints the map of coordinates
            print('first player you choose where to place -x\nsecond player you choose where to place -o\n ')

            while True:  # while that running the initial game
                print('Player 1 your turn, please choose where to put-x \n')
                while True:  # while for player 1 turn
                    try:
                        Row = int(input("first Enter row : "))  # choosing row where to place x
                    except ValueError:
                        continue
                    try:
                        Line = int(input("now Enter line : "))  # choosing row where to place y
                    except ValueError:
                        continue
                    if (Row not in range(len(Game_Board))) or (
                            Line not in range(len(Game_Board))):  # check coordinates if in range
                        print(f'please enter valid number between 0 - {(len(Game_Board) - 1)}\n')
                    elif Game_Board[Row][Line] != '_':  # check if this square is already taken
                        print(f'this square {Row}{Line} is already taken please choose other one')
                    else:
                        Game_Board[Row][Line] = 'x'  # insert the symbol of the player in the coordinates chose
                        counter_for_draw += 1  # counter up for draw
                        break

                current(Game_Board)  # calls the current function to show the current board situation
                current(Game_map)  # calls the current function to show the map

                if 'y' in player2_help:  # if for help player 2, if player 2 choose help
                    if win_check(Game_Board) == 'x':  # first check if player 1 winner after move
                        print('player 1 you are the winner!!!!!!!!!!!!!!!\n')
                        break
                    else:
                        win_check(Game_Board, 2)  # if player 1 not win help player 2

                elif win_check(Game_Board) == 'x':  # first check if player 1 winner after move
                    print('player 1 you are the winner!!!!!!!!!!!!!!!\n')

                if counter_for_draw == (len(Game_Board) ** 2):  # draw check if now squares left in case no one wins
                    print('Its a Draw no one wins :)\n')
                    break

                print('Player 2 your turn, please choose where to put-o \n')

                while True:  # while for turn of player 2
                    try:
                        Row = int(input("first Enter row : "))  # coordinates choose
                    except ValueError:
                        continue
                    try:
                        Line = int(input("now Enter line : "))  # coordinates choose
                    except ValueError:
                        continue
                    if (Row not in range(len(Game_Board))) or (
                            Line not in range(len(Game_Board))):  # check coordinates if in range
                        print(f'please enter valid number between 0 - {(len(Game_Board) - 1)}\n')
                    elif Game_Board[Row][Line] != '_':  # check if this square is already taken
                        print(f'this square {Row}{Line} is already taken please choose other one\n')
                    else:
                        Game_Board[Row][Line] = 'o'  # insert the symbol of the player in the coordinates chose
                        counter_for_draw += 1
                        break

                current(Game_Board)  # calls the current function to show the board
                current(Game_map)  # calls the current function to show the map

                if 'y' in player1_help:  # if for help player 1, if player 1 choose help
                    if win_check(Game_Board) == 'o':  # winner check with win_check function
                        print('player 2 you are the winner!!!!!!!!!!!!!!!\n')  # check if player 2 is the winner
                        break
                    else:
                        win_check(Game_Board, 1)  # if player 2 didn't win, help player 1 for next move

                elif win_check(Game_Board) == 'o':  # winner check with win_check function
                    print('player 2 you are the winner!!!!!!!!!!!!!!!\n')
                    break

                if counter_for_draw == (len(Game_Board) ** 2):  # draw check if now squares left in case no one wins
                    print('Its a Draw no one wins :)\n')
                    break

            while True:  # while for input if players want replay
                replay = input('wanna replay? y/n : ')
                if replay in ['y', 'n']:
                    print(f'user typed {replay} returning to main menu\n')
                    break
                else:
                    print('Type y or n')
                    continue
            if replay == 'n':
                break

    if Menu == 2:  # if for menu choose number 1 - player vs player
        while True:  # while that runs the player vs player game
            player1_help = ''  # declare and reset help variable for player 1
            player2_help = ''  # declare and reset help variable for player 2
            Player = 0  # reset the variable that for choosing which player when player vs computer
            replay = ''  # reset the choice  if to replay the match
            cord = ''  # declare and reset cord help variable for showing coordinates on the help map
            board_size = 0
            Game_Board = []
            Game_map = []

            counter_for_draw = 0  # reset draw counter
            print('welcome to player vs computer \n')

            while True:
                try:
                    Player = int(input('please choose first player (place x) or second player (place o) 1/2 : '))
                except ValueError:
                    print('please insert choose 1 or 2 \n')
                    continue
                if Player == 1 or Player == 2:
                    break

            if Player == 1:  # player choose to be player 1 and put 'x'
                while True:  # while that runs the player vs player game
                    board_size = 0
                    Game_Board = []
                    Game_map = []
                    counter_for_draw = 0  # reset draw counter
                    while True:  # while for input help player 1.
                        player1_help = input('Player 1 Do you want help during the game? y/n : ')
                        if player1_help in ['y', 'n']:
                            print(f'user typed {player1_help}')
                            break
                        else:
                            print('Type y or n')
                            continue

                    while True:  # while for checking the input of the size of the game board, so it will be 3-9 only
                        try:
                            Board_size = int(input('please select board size from 3 to 9 : '))  # choose  size of board
                        except ValueError:
                            continue
                        if 2 < Board_size < 10:  # check if the input within the range of 3-9
                            for x in range(Board_size):  # if yes, for in for to construct the game board
                                help_list = []
                                for b in range(Board_size):  # for this I am using two lists and append them
                                    help_list.append('_')
                                Game_Board.append(help_list)

                            for o in range(Board_size):  # now I will construct the map of game board
                                help_list = []
                                for p in range(Board_size):  # using again two for loops, and two lists
                                    cord = '{}{}'.format(o, p)
                                    help_list.append(cord)
                                Game_map.append(help_list)

                            if Board_size == len(Game_Board):  # if all ok move break the while of board creation
                                print('\n')
                                break
                        else:
                            print('please try again')
                    current(Game_Board)  # prints  the game board
                    current(Game_map)  # prints the map of coordinates
                    print('first player you choose where to place -x\nsecond player you choose where to place -o\n ')

                    while True:  # while that running the initial game
                        print('Player 1 your turn, please choose where to put-x \n')
                        while True:  # while for player 1 turn
                            try:
                                Row = int(input("first Enter row : "))  # choosing row where to place x
                            except ValueError:
                                continue
                            try:
                                Line = int(input("now Enter line : "))  # choosing row where to place y
                            except ValueError:
                                continue
                            if (Row not in range(len(Game_Board))) or (
                                    Line not in range(len(Game_Board))):  # check coordinates if in range
                                print(f'please enter valid number between 0 - {(len(Game_Board) - 1)}\n')
                            elif Game_Board[Row][Line] != '_':  # check if this square is already taken
                                print(f'this square {Row}{Line} is already taken please choose other one')
                            else:
                                Game_Board[Row][Line] = 'x'  # insert the symbol of the player in the coordinates chose
                                counter_for_draw += 1  # counter up for draw
                                break

                        current(Game_Board)  # calls the current function to show the current board situation
                        current(Game_map)  # calls the current function to show the
                        if win_check(Game_Board) == 'x':  # first check if player 1 winner after
                            print('player 1 you are the winner!!!!!!!!!!!!!!!\n')
                            break

                        if counter_for_draw == (
                                len(Game_Board) ** 2):  # draw check if now squares left in case no one wins
                            print('Its a Draw no one wins :)\n')
                            break

                        print('Player 2 your turn, please choose where to put-o \n')

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

                        if 'y' in player1_help:  # if for help player 1, if player 1 choose help
                            if win_check(Game_Board) == 'o':  # winner check with win_check function
                                print(
                                    'you lose, computer is the winner!!!!!!!!!!!!!!!\n')  # check if the winner
                                break
                            else:
                                win_check(Game_Board, 1)  # if player 2 didn't win, help player 1 for next move

                        elif win_check(Game_Board) == 'o':  # winner check with win_check function
                            print('player 2 you are the winner!!!!!!!!!!!!!!!\n')
                            break

                        if counter_for_draw == (len(Game_Board) ** 2):  # draw check
                            print('Its a Draw no one wins :)\n')
                            break

                    while True:  # while for input if players want replay
                        replay = input('wanna replay? y/n : ')
                        if replay in ['y', 'n']:
                            break
                        else:
                            print('Type y or n')
                            continue
                    if replay == 'n':
                        print(f'user typed {replay} returning to main menu\n')
                        break
                    elif replay == 'y':
                        continue
                if replay == 'n':
                    break

            if Player == 2:  # player choose to be player 2 and put 'o'
                while True:  # while that runs the player vs player game
                    board_size = 0
                    Game_Board = []
                    Game_map = []
                    counter_for_draw = 0  # reset draw counter
                    while True:  # while for input help player 2
                        player2_help = input('Player 2 Do you want help during the game? y/n : ')
                        if player2_help in ['y', 'n']:
                            print(f'user typed {player1_help}')
                            break
                        else:
                            print('Type y or n')
                            continue

                    while True:  # while for checking the input of the size of the game board, so it will be 3-9 only

                        try:
                            Board_size = int(input('please select board size from 3 to 9 : '))  # choose  size of board
                        except ValueError:
                            continue
                        if 2 < Board_size < 10:  # check if the input within the range of 3-9
                            for x in range(Board_size):  # if yes, for in for to construct the game board
                                help_list = []
                                for b in range(Board_size):  # for this I am using two lists and append them
                                    help_list.append('_')
                                Game_Board.append(help_list)

                            for o in range(Board_size):  # now I will construct the map of game board
                                help_list = []
                                for p in range(Board_size):  # using again two for loops, and two lists
                                    cord = '{}{}'.format(o, p)
                                    help_list.append(cord)
                                Game_map.append(help_list)

                            if Board_size == len(Game_Board):  # if all ok move break the while of board creation
                                print('\n')
                                break
                        else:
                            print('please try again')
                    current(Game_Board)  # prints  the game board
                    current(Game_map)  # prints the map of coordinates

                    while True:  # while that running the initial game
                        print(
                            'first player you choose where to place -x\nsecond player you choose where to place -o\n ')

                        print('now its the computer turn  \n')
                        while True:  # while for turn of player 1
                            Row = random.randrange(0, len(Game_Board))  # coordinates choose
                            Line = random.randrange(0, len(Game_Board))  # coordinates choose
                            if Game_Board[Row][Line] == '_':  # check if this square is already taken
                                Game_Board[Row][Line] = 'x'  # insert the symbol of the player in the coordinates chose
                                counter_for_draw += 1
                                break

                        current(Game_Board)  # calls the current function to show the current board situation
                        current(Game_map)  # calls the current function to show the map

                        if 'y' in player2_help:  # if for help player 2, if player 2 choose help
                            if win_check(Game_Board) == 'x':  # first check if player 1 winner after move
                                print('you lose, the computer is the winner!!!!!!!!!!!!!!!\n')
                                break
                            else:
                                win_check(Game_Board, 2)  # if player 1 not win help player 2

                        elif win_check(Game_Board) == 'x':  # first check if player 1 winner after move
                            print('you lose, the computer is the winner!!!!!!!!!!!!!!!\n')

                        if counter_for_draw == (
                                len(Game_Board) ** 2):  # draw check if now squares left in case no one wins
                            print('Its a Draw no one wins :)\n')
                            break

                        print('Player 2 your turn, please choose where to put-o \n')

                        while True:  # while for turn of player 2
                            try:
                                Row = int(input("first Enter row : "))  # coordinates choose
                            except ValueError:
                                continue
                            try:
                                Line = int(input("now Enter line : "))  # coordinates choose
                            except ValueError:
                                continue
                            print('\n')
                            if (Row not in range(len(Game_Board))) or (
                                    Line not in range(len(Game_Board))):  # check coordinates if in range
                                print(f'please enter valid number between 0 - {(len(Game_Board) - 1)}\n')
                            elif Game_Board[Row][Line] != '_':  # check if this square is already taken
                                print(f'this square {Row}{Line} is already taken please choose other one\n')
                            else:
                                Game_Board[Row][Line] = 'o'  # insert the symbol of the player in the coordinates chose
                                counter_for_draw += 1
                                break

                        current(Game_Board)  # calls the current function to show the board
                        current(Game_map)  # calls the current function to show the map

                        if win_check(Game_Board) == 'o':  # winner check with win_check function
                            print('player 2 you are the winner!!!!!!!!!!!!!!!\n')
                            break

                        if counter_for_draw == (
                                len(Game_Board) ** 2):  # draw check if now squares left in case no one wins
                            print('Its a Draw no one wins :)\n')
                            break

                    while True:  # while for input if players want replay
                        replay = input('wanna replay? y/n : ')
                        if replay in ['y', 'n']:
                            break
                        else:
                            print('Type y or n')
                            continue
                    if replay == 'n':
                        break
                    elif replay == 'y':
                        continue
                if replay == 'n':
                    print(f'user typed {replay} returning to main menu\n')
                    break

    elif Menu == 3:
        while True:
            board_size = 0
            Game_Board = []
            Game_map = []
            counter_for_draw = 0  # reset draw counter
            print('welcome to computer vs computer \n')
            while True:  # while for checking the input of the size of the game board, so it will be 3-9 only
                try:
                    Board_size = int(input('please select board size from 3 to 9 : '))  # choose  size of board
                except ValueError:
                    continue
                if 2 < Board_size < 10:  # check if the input within the range of 3-9
                    for x in range(Board_size):  # if yes, for in for to construct the game board
                        help_list = []
                        for b in range(Board_size):  # for this I am using two lists and append them
                            help_list.append('_')
                        Game_Board.append(help_list)

                    for o in range(Board_size):  # now I will construct the map of game board
                        help_list = []
                        for p in range(Board_size):  # using again two for loops, and two lists
                            cord = '{}{}'.format(o, p)
                            help_list.append(cord)
                        Game_map.append(help_list)

                    if Board_size == len(Game_Board):  # if all ok move break the while of board creation
                        print('\n')
                        break
                else:
                    print('please try again')
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
                    print('Its a Draw no one wins :)\n')
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
                    print('Its a Draw no one wins :)\n')
                    break
                time.sleep(3)

            while True:  # while for input if players want replay
                replay = input('wanna replay? y/n : ')
                if replay in ['y', 'n']:
                    break
                else:
                    print('Type y or n')
                    continue
            if replay == 'n':
                break
            elif replay == 'y':
                continue

    elif Menu == 4:
        print('Goodbye')
        Program_Run = False
