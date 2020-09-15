from random import randint
#Empty board
board = []

#Need 5x5 board
for i in range(5):
    board.append(["O"] *5)
   
    

#Separate into 5 rows of O and remove commas
def board_setup(board):
    for row in board:
        print(" ".join(row))
board_setup(board)

#Define ship's position using random numbers

def random_row(board):
    return randint(0,len(board) - 1)
    
def random_column(board):
    return randint(0,len(board) - 1)

r = random_row(board)
c = random_column(board)



print("Let's play Battleships!")



for turn in range(4):
    
#User inputs their guesses for row and column numbers
    guess_row = int(input("Guess Row (0 to " + str(len(board) -1) + "): "))
    guess_col = int(input("Guess Column (0 to " + str(len(board) -1) + "): "))

#Check the guesses
    print("Turn", turn + 1)
    if guess_row==r and guess_col==c:
        print("Congratulations! You sank my battleship!")
        break
    
    else:
        
        if guess_row not in range(len(board)) or guess_col not in range(len(board)):
            print("Oops, that's not even in the ocean!")
        elif board[guess_row][guess_col]=="X":
            print("You guessed that one already!")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col]="X"
        board_setup(board)

    if turn == 3:
        print("Game Over")
        input("Press any key to close")
