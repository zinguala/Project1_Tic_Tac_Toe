#function:
def current(*args): #prints the current board situation with map
    for i in range((len(args))):
        for k in range(len(args[i])):
            print(*args[i][k], sep =' | ') #print the strint without to queots ''

    return None

#main code:
Game_Board=[['_', '_', '_', ], ['_', '_', '_'], ['_', '_', '_']]
print(Game_Board)
current(Game_Board)