import random

grid = []
cols = 7
turn = None


print("Welcome to Virtual Connect 4. A Virtual Version of the popular Game. The object of the game is to get 4 of your chips in a row. Vertical, Diagonal, and Horizontal Lines all count as a win. Coded by Maxwell Hunt, with help from Dragos Baciu-David (Please don't sue me) Remember to tip your programmer. (That's me) ")
  
def CreateGrid():
  tempGrid = [];
  for i in range(cols):
    tempGrid.append([])
    for j in range(15):
      if(i < 6):
        if(j % 2 == 0):
          tempGrid[i].append("|")
        else:
          tempGrid[i].append(" ")
      else:
        tempGrid[i].append("-")
  return tempGrid
  
grid = CreateGrid()
  
def Drop(column, color):
  row = len(grid) - 2
  while True:
    if(grid[row][(column*2) - 1] == " "):
      grid[row][(column*2) - 1] = color
      break
    else:
      row -= 1
      
def CheckWin():
  for i in range(len(grid) - 1):
    # CheckVertical Win
    for j in range(len(grid[i])):
      if(i > 2):
        if(j % 2 != 0):
          c = grid[i][j]
          if(grid[i - 1][j] == c and grid[i - 2][j] == c and grid[i - 3][j] == c and c != " "):
            return True
            
      # CheckDiagonalLeft Win
      if(j >= (4*2) - 1):
        if(j % 2 != 0):
          c = grid[i][j]
          if(grid[i-1][j - 2] == c and grid[i-2][j - 4] == c and grid[i - 3][j - 6] == c and c != " "):
            return True
            
    # CheckDiagonalRight Win
    for j in range(((cols - 3)*2)):
      if(i > 2):
        if(j % 2 != 0):
          c = grid[i][j]
          if(grid[i - 1][j + 2] == c and grid[i - 2][j + 4] == c and grid[i - 3][j + 6] == c and c != " "):
            return True
            
      # CheckHorizontal Win
      if(j % 2 != 0):
        c = grid[i][j]
        if(grid[i][j + 2] == c and grid[i][j + 4] == c and grid[i][j + 6] == c and c != " "):
          return True
              
def PrintGrid():
  print("")
  print("  1   2   3   4   5   6   7")
  for i in range(len(grid)):
    print(*grid[i])
    
def ClearBoard():
  for i in range(len(grid) - 1):
    for j in range(len(grid[i])):
      if(j % 2 != 0):
        grid[i][j] = " "

def Main():
  print("")
  whoGoesFirst = input("What colour goes first, r for red y for yellow")
  
  if(whoGoesFirst == "r"):
    turn = 1
  elif(whoGoesFirst == "y"):
    turn = -1
  else:
    turn = random.randint(0,1)
  
  if(turn == 0):
    turn = -1
  while True:
    if(CheckWin()):
      PrintGrid()
      if(turn == 1):
        print("Yellow Player wins")
      else:
        print("Red Player wins")
      playAgain = input("wanna play again y for yes n for no")
      
      if(playAgain == "y"):
       ClearBoard()
      else:
        print("")
        print("Thank You so much for playing this game, I'm not quite sure why I'm thanking you for litterally playing a video game but I'm gonna thank you anyway")
        break
    else:
      PrintGrid()
      if(turn == 1):
        
        try:
          PlayerMove = int(input("Red Player Enter a collumn 1-7: "))
        except:
         
          print("")
          print("Poor spelling and typing skills are highly frowned upon. For this reason we will be punishing you for your carelessness. Seriously it's not that hard, all you had to do was litterally type a number. You failed. Therefore I will be punishing you by doing this")
          print("")
          print("Yellow Player Wins")
          break
        
        while (PlayerMove < 1 or PlayerMove > 7):
          print("That column doesn't exist")
          try:
            PlayerMove = int(input("Red Player Go Again"))
          except:
            PlayerMove = int(input("Enter a valid number"))
        
        while (grid[0][PlayerMove*2 - 1] != " "):
          print("Sorry, that Collumns full")
          try:
            PlayerMove = int(input("Red player Go Again"))
          except:
            PlayerMove = int(input("Enter a valid number"))
          
          
        Drop(PlayerMove,"R")
        turn *= -1
      elif(turn == -1):
        try:
          PlayerMove = int(input("Yellow Player Enter a column 1-7: "))
        except:
          print("")
          print("Poor spelling and typing skills are highly frowned upon, therefore we will be punishing you in order to improve your finger accuracy. Seriously all you needed to do was hit one of the number keys. Anywho, I will be punishing you by doing this")
          print("")
          print("Red Player wins")
          break

          
        while (PlayerMove < 1 or PlayerMove > 7):
          print("That column doesn't exist")
          try:
            PlayerMove = int(input("Yellow Player Go Again"))
          except:
            PlayerMove = int(input("Enter a valid number"))
        
        while (grid[0][PlayerMove *2 - 1] != " "):
          print("Sorry, that Collumns full")
          try:
            PlayerMove = int(input("Yellow Player Go Again"))
          except:
            PlayerMove = int(input("Enter a valid number"))
        Drop(PlayerMove,"Y")
        turn *= -1

Main()