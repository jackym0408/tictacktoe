# create board
# display the board

#handle input
#update board

#check win
#check rows
# check col.
# check Diag.

currentPlayer = "X"
gameRunning = True
winner = None

board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handleInput():
  
  valid = False 

  pos = input("Choose a position 1-9: ")

  while not valid: 
    while pos not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      pos = input("That position is invalid! Please choose a position from 1-9: ")

    pos = int(pos) - 1
    if board[pos] != "-":
      print("You can't get there!")
    else: 
      valid = True

  board[pos] = currentPlayer

  displayBoard()

  return

def checkRows(): 
  global gameRunning

  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"

  if row1 or row2 or row3: 
    gameRunning = False

  if row1: 
    return board[0]
  elif row2:
    return board[3]
  elif row3: 
    return board[6]
  else: 
    return None


def checkCols():
  global gameRunning

  cols1 = board[0] == board[3] == board[6] != "-"
  cols2 = board[1] == board[4] == board[7] != "-"
  cols3 = board[2] == board[5] == board[8] != "-"

  if cols1 or cols2 or cols3: 
    gameRunning = False

  if cols1: 
    return board[0]
  elif cols2:
    return board[1]
  elif cols3: 
    return board[2]
  else: 
    return None 

def checkDiags():
  global gameRunning

  diags1 = board[0] == board[4] == board[8] != "-"
  diags2 = board[2] == board[4] == board[6] != "-"
  

  if diags1 or diags2: 
    gameRunning = False

  if diags1: 
    return board[0]
  elif diags2:
    return board[2]
  else: 
    return None 


def checkWin():
  global winner

  if checkRows():
    winner = checkRows()
  elif checkCols():
    winner = checkCols()
  elif checkDiags():
    winner = checkDiags()
  else: 
    winner = None

  return winner

def checkTie():
  global gameRunning 

  if "-" not in board:
    gameRunning = False

def checkGameOver():
  checkWin()
  checkTie()
  return

def flipPlayers():

  global currentPlayer

  if currentPlayer == "X":
    currentPlayer = "O"
  else: 
    currentPlayer = "X"
    
  return 

def playGame():
  displayBoard()

  while gameRunning:
    handleInput()
    checkGameOver()
    flipPlayers()

  if winner == "X" or winner == "O": 
    print(winner + " 's won! ")
  else:
    print("TIE!")

playGame()
