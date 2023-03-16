from goto import goto, comefrom, label
#function:
def current(*args): #prints the current board situation with map
    for i in range((len(args))):
        for k in range(len(args[i])):
            print(*args[i][k], sep =' | ') #print the string without to quotes '' and print map
    return None


#main code:
lable1:
Win = False
Menu=0
while Win == False:
    Game_Board = [['_', '_', '_', ], ['_', '_', '_'], ['_', '_', '_']]
    print('Welcome noughts and crosses :) \nTo Choose which game you want to play press: \n 1-player vs player\n'
          ' 2-player vs computer\n 3-computer vs computer\n 4-exit\n')
    Menu= int(input('please choose now : '))

    if Menu==1:
        print('first player you choose where to place -x\nsecond player you choose where to place -o ')
    else:
        goto lable1;

    break
