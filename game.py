#!python

from sys import exit
from random import randint

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
        while True: 
            yesno = input("Would you like to play again (y/n)?" ).upper()
            if yesno in ("Y","YES"):
                break
            if yesno in ("N","NO"):
                playing = False
                break

def runGame(name, board):
    currPos = -1
    size = len(board)
    target = size * size + 1
    mark = f" {name[0]}  "
    while True:
        lastPos = currPos
        throw = randint(1,size+1)
        currPos += throw
        print(f"You threw a {throw}.")
# If still in first row, just place at random
        if currPos < size + 1:
            currPos = randint(0,size) + 1
            print(f"Sorry, still stuck in the start row at position {currPos}.")
# Check if we hit the target and won            
        elif currPos == target:
            print(f"Congratulations, {name}, you won!")
            return
# Bad luck, we overstepped the end - go backwards instead
        elif currPos > target:
            currPos -= 2*throw
            print(f"Sorry, overshot -- go back to {currPos}.")
        else:
            print(f"Looks good -- you're now at position  {currPos}.")
        board = moveMe(board,size,lastPos,"    ")
        board = moveMe(board,size,currPos,mark)
        pMat(board)
        x = input("Enter for next move, anything else (like q) to quit?: ")
        if x != "":
            return

def moveMe(board,size,pos,text):
    pos -= 1
    row = pos // size
    col = pos % size
    board[row][col] = text
    return board

def pMat(matrix):
    for row in matrix:
        print(row)

def getName(size):
    # return "Brent"
    name = input("Hi! What's your name (enter to stop)?: ")
    if name == "":
        print(f"Thanks, see you later!")
        exit()
    name = name[0].upper() + name[1:].lower()
    print(f"Hi, {name}! Today we are playing {size} x {size}")
    print(f"Your marker is '{name[0]}'")
    return name

def main():
# Set up environment
    size = 5
    name = getName(size)
# Play the game
    gPlay(size, name)

main()
