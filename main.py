# functions:----------------------------------------------------------------
def current(*args):  # prints the current board situation with map
    for i in range((len(args))):
        for k in range(len(args[i])):
            print(*args[i][k], sep=' | ')  # print the string without to quotes ''
    return None


def game_map(args):
    for i in range(len(args)):
        for k in range(args):
            print(f'{i},{k}', end=' | ')
            print('')


def win_check(args):  # function for win check if player wins it returns the symbol of the winner if not return None.
    count_for_win = len(args)           # set how many symbols in a sequence for wining
    count_line_x = 0                    # initialize the counter for x in one line
    count_line_o = 0                    # initialize the counter for o in one line
    for i in range(len(args)):
        count_row_x = 0  # rest the count for new row check 'x'
        count_row_o = 0  # rest the count for new row check 'o'
        for k in range(len(args)):     # row check for win
            if args[i][k] != '_':
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


    return None


# main code:-----------------------------------------------------------------------------------
Program_Run = True  # for running while that runs the whole Program until hitting exit.
Menu = 0            # varible for a menu so the player can choose
while Program_Run:
    Game_Run = True  # for resetting the Game finish after game is ended to start again.
    Game_Board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    print('Welcome noughts and crosses :) \nTo Choose which game you want to play press: \n 1-player vs player\n'
          ' 2-player vs computer\n 3-computer vs computer\n 4-exit\n')
    Menu = int(input('please choose now : '))

    if Menu == 1:
        print('first player you choose where to place -x\nsecond player you choose where to place -o\n ')
        while Game_Run:
            print('Player 1 your turn, please choose where to put-x \n')
            Row = int(input("first Enter row : "))
            Line = int(input("now Enter line : "))
            if (Row not in range(len(Game_Board))) or (Line not in range(len(Game_Board))):
                print('please enter valid number between 0-2\n')
            else:
                Game_Board[Row][Line] = 'x'
                current(Game_Board)
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
            if win_check(Game_Board) == 'o':
                print('player 2 you are the winner')
                break





