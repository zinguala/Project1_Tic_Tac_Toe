# functions:----------------------------------------------------------------------------------------
def current(*args):  # prints the current board situation with map
    for i in range((len(args))):
        for k in range(len(args[i])):
            print(*args[i][k], sep=' | ')  # print the string without to quotes ''
    return None

def win_check(args):  # function for win check if player wins it returns the symbol of the winner if not return None.
    count_for_win = len(args)           # set how many symbols in a sequence for wining
    count_line_x = 0                    # declare the counter for x in one line
    count_line_o = 0                    # declare the counter for o in one line
    count_first_diagonal_x = 0            # declare the count for first (00,11,22,33,....) diagonal check 'x'
    count_first_diagonal_o = 0              # declare the count for first (00,11,22,33,....) diagonal check 'o'
    count_second_diagonal_x = 0              # declare the count for second diagonal (x0,..,21,12,..,0x) check 'x'
    count_second_diagonal_o = 0              # declare the count for second diagonal (x0,..,21,12,..,0x) check 'o'
    for i in range(len(args)):
        count_row_x = 0  # declare and rest the count for new row check 'x'
        count_row_o = 0  # declare and rest the count for new row check 'o'
        for k in range(len(args)):     # row check for win
            if args[i][k] != '_':      # first check if this place is empty, if yes skip row check and one diagonal check
                if args[i][k] == 'x':
                    count_row_x += 1       # count 1 up when there is x in this place
                    if count_row_x == count_for_win:         # see if the x counter in row reached to the limit for win
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
                    if count_row_o == count_for_win:        # see if the o counter in line reached to the limit for win
                        return 'o'
                if i == k:     #check the first diagonal (00,11,22,33,....) for sequence in one symbol
                    if args[i][k] == 'x':
                        count_first_diagonal_x += 1    # count 1 up when there is x in this place
                        if count_first_diagonal_x == count_for_win:
                            return 'x'
                    elif args[i][k] == 'o':
                        count_first_diagonal_o += 1     # count 1 up when there is o in this place
                        if count_first_diagonal_o == count_for_win:
                            return 'o'

    for j in range(len(args)):                 #new for the second diagonal check
        if args[count_for_win - j - 1][j] == 'x':  # check the second diagonal (x0,..,21,12,..,0x) for sequence in one symbol
            count_second_diagonal_x += 1
            if count_second_diagonal_x == count_for_win:
                return 'x'
        elif args[count_for_win - j - 1][j] == 'o':
            count_second_diagonal_o += 1
            if count_second_diagonal_x == count_for_win:
                return 'o'
    return None


# main code:---------------------------------------------------------------------------------------------
Program_Run = True  # for running while that runs the whole Program until hitting exit.
Menu = 0            # varible for a menu so the player can choose
Game_Board_size3 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
Game_map_size3 = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]
Game_board_size4 = [['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']]
Game_map_size4 = [['00', '01', '02', '03'], ['10', '11', '12', '13'], ['20', '21', '22', '23'],
                        ['30', '31', '32', '33']]

while Program_Run:
    Game_Board = []
    Game_map = []
    print('Welcome noughts and crosses :) \nTo Choose which game you want to play press: \n 1-player vs player\n'
          ' 2-player vs computer\n 3-computer vs computer\n 4-exit\n')
    Menu = int(input('please choose now : '))
    if Menu == 1:
        while True:
            try:
                Board_size = int(input('please select board size 3 or 4 : '))
            except ValueError:
                continue
            if Board_size == 3:
                print(f'You choose size: {Board_size}x{Board_size}')
                Game_Board = Game_Board_size3
                Game_map = Game_map_size3
                break
            if Board_size == 4:
                Game_Board = Game_board_size4
                Game_map = Game_map_size4
                break
        while True:
            print('first player you choose where to place -x\nsecond player you choose where to place -o\n ')
            print('Player 1 your turn, please choose where to put-x \n')

            Row = int(input("first Enter row : "))
            Line = int(input("now Enter line : "))
            if (Row not in range(len(Game_Board))) or (Line not in range(len(Game_Board))):
                print('please enter valid number between 0-2\n')
            else:
                Game_Board[Row][Line] = 'x'
                current(Game_Board)
                current(Game_map)
                if win_check(Game_Board) == 'x':
                    print('player 1 you are the winner')
                    break
                print('Player 2 your turn, please choose where to put-o \n')
                Row = int(input("first Enter row : "))
                Line = int(input("now Enter line : "))
                if (Row not in range(len(Game_Board))) or (Line not in range(len(Game_Board))):
                    print('please enter valid number between 0-2\n')
                else:
                    Game_Board[Row][Line] = 'o'
                    current(Game_Board)
                    current(Game_map)
                    if win_check(Game_Board) == 'o':
                        print('player 2 you are the winner')
                        break




