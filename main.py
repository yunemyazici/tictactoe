import random
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    inp = int(input("Enter the spot(1-9): "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("you can't do that move!")printboard
        playerInput(board)

def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie.")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiag(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def main():
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()

if __name__ == "__main__":
    main()
