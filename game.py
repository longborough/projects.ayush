#!python

def main():
# Set up environment
    size = 5
    name = getName(size)
# Play the game
    gPlay(size, name)

# gPlay is the game loop
# When a game ends, it asks the player whether they want to pla again,
# returning True if yes and False if no.
def gPlay(size, name):
    playing = True
    while playing:
        board = [ [f"{x+y+1:3d} " for x in range(0,size)]
                  for y in range(0,size*size,size) ]
        pMat(board)
        board = [ ["    " for x in range(0,size)]
                  for y in range(0,size*size,size) ]
        runGame(name, board)
        playing = False
    return undefined()

def runGame(name, board):
    return undefined()

def getName(size):
    name = input("Hi! What's your name (enter to stop)?: ")
    if name == "":
        print(f"Thanks, see you later!")
        exit()
    name = name[0].upper() + name[1:].lower()
    print(f"Hi, {name}! Today we are playing {size} x {size}")
    print(f"Your marker is '{name[0]}'")
    return name

def pMat(matrix):
    for row in matrix:
        print(row)

def undefined():
    print("Undefined called")
    return None

main()
