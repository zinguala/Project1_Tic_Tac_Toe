
#functions:
def current(*args): #prints the current board situation with map
    for i in range((len(args))):
        for k in range(len(args[i])):
            print(*args[i][k], sep =' | ') #print the string without to quotes ''


    return None

def game_map():
    for i in range(0,3):
        for k in range(0,3):
            print(f'{i},{k}',end=' | ')
        print('')

def win_check(*args):
    for i in range(len(args)):
        return None







#main code:
Program_Run= True #for running while that runs the whole Program until hitting exit.
Menu=0
while Program_Run:
    Game_Run = True #for resetting the Game finish after game is ended to start again.
    Game_Board = [['_', '_', '_', ], ['_', '_', '_'], ['_', '_', '_']]
    print('Welcome noughts and crosses :) \nTo Choose which game you want to play press: \n 1-player vs player\n'
          ' 2-player vs computer\n 3-computer vs computer\n 4-exit\n')
    Menu= int(input('please choose now : '))

    if Menu==1:
        print('first player you choose where to place -x\nsecond player you choose where to place -o\n ')
        while Game_Run :
            print('Player 1 your turn, please choose where to put-x \n')
            Row = int(input("first Enter row : "))
            Line = int(input("now Enter line : "))
            if (Row not in range(len(Game_Board))) or (Line not in range(len(Game_Board))):
                print('please enter valid number between 0-2\n'')
            else:
                Game_Board[Row][Line]='x'
                current(Game_Board)




    break
