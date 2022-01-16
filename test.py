#I accidentally coded this all by myself before I knew we were supposed to work in groups, so this code is all mine (Aiden Edwards)


#global variables
numMoves = 0
winNum = int(input('Enter a board size (3 or greater): '))


def main():
    #initializes the board based on a user input, and initializes that x's go first
    board = boardInit(winNum)
    playerTile = 'x'
    #checks to see that no win conditions are satisfied, and also whether or not the board is a draw
    while not checkWin(board) and numMoves < 9:
        printBoard(board)
        print(playerTile + "'s turn")
        userInput = input('Pick a number (1 - ' + str((winNum * winNum)) + '): ')
        userInput = int(userInput)
        playerTile = addMove(userInput, winNum, playerTile, board)
        checkWin(board)
    printBoard(board)
    #if statement is needed because otherwise the "playerTile wins!" would display the wrong tile
    if numMoves != ((winNum * winNum) - 1):
        if playerTile == 'x':
            playerTile ='o'
        else:
            playerTile = 'x'
        print(playerTile + ' wins!')
    else:
        print("It's a draw!")
    print('Game over')

#initializes the board based on how big the board is that the user wanted to play
def boardInit(num):
    board = []
    boardRow = []
    #the user input squared is the amount of squares in the board, so the loop goes by row and fills all those positions
    for i in range(0,(num * num)):
        boardRow.insert(num,i + 1)
        if (i + 1) % num == 0:
            board.insert(num,boardRow)
            boardRow = []
    return board
        
    
#iterates through the arrays and prints every value
def printBoard(board):
    for i in range(0,winNum):
        print('-----------------------')
        for j in range(0,winNum):
            print(end = ' ')
            print (board[i][j],end=" |")
        
        print(' ')

        

def checkWin(board):
    #checks win conditions
    if checkCol(board):
        return True
    if checkRow(board):
        return True
    if checkDiag(board):
        return True
    return False

#if o's equals the win number in a row (in this case 3), then o's win. x's have to get the negative of the win number, otherwise neither win
def checkCol(board):
    #checks for each index from 0 to the number a player needs in a row to win
    for i in range(0,winNum):
        score = 0
        for j in range(0,winNum):
            if(board[i][j] == 'o'):
                score = score + 1
            if(board[i][j] == 'x'):
                score = score - 1
            if(score == winNum or score == -1*winNum):
                return True

#same logic as checkCol(), this just compares the items in the row
def checkRow(board):
    for i in range(0,winNum):
        score = 0
        for j in range(0,winNum):
            if(board[j][i] == 'o'):
                score = score + 1
            if(board[j][i] == 'x'):
                score = score - 1
            if(score == winNum or score == -1*winNum):
                return True
                break

#the diagonals are the same row and column, or add up to get the last index, so loops were used
def checkDiag(board):  
    score = 0      
    for i in range(0,winNum):
        if(board[i][i] == 'o'):
            score = score + 1
        if(board[i][i] == 'x'):
            score = score - 1
        if(score == winNum or score == -1*winNum):
            return True
    score = 0
    for i in range(0,winNum):
        if(board[i][(winNum - 1) - i] == 'o'):
            score = score + 1
        if(board[i][(winNum - 1) - i] == 'x'):
            score = score - 1
        if(score == winNum or score == -1*winNum):
            return True
    return False

#replaces a number in the matrix with a player tile
def addMove(num, winNum, playerTile, board):
    global numMoves
    for i in range(0,winNum):
        for j in range(0,winNum):
            if board[i][j] == num:
                board[i][j] = playerTile
                if playerTile == 'o':
                    playerTile = 'x'
                    numMoves = numMoves + 1
                    return playerTile
                if playerTile == 'x':
                    playerTile = 'o'
                    numMoves = numMoves + 1
                    return playerTile
    return playerTile

#call to the main() function. Just runs all the code
main()