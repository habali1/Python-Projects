#XOX
#Game starts with X's player placing location which is from 0 to 2 top to bottom
#and 0 to 2 left to right. Once X's player enters two locations like: "0,3"
#that section is not going to be available like XOX game, so Y player needs to
#enter a diffrent location. Person that makes 3 X's or 3 Y's wins the game.
board=[[" "," "," "],[" "," "," "],[" "," "," "]]

def capraz():
  for i in range(3):
    for j in range(3):
      if board[i][j]==" ":
        if board[0][0]==board[1][1]==board[2][2]!=" ":
          print("The person who is: ",board[x][y],"wins")
          return True
        elif board[0][2]==board[1][1]==board[2][0]!=" ":
          print("The person who is: ",board[x][y],"wins")
          return True
        else:
          return False
def dikey():
  for i in range(3):
    for j in range(3):
      if board[i][j]==" ":
        if board[0][0]==board[1][0]==board[2][0]!=" ":
          print("The person who is: ",board[x][y],"wins")
          return True
        elif board[0][1]==board[1][1]==board[2][1]!=" ":
          print("The person who is: ",board[x][y],"wins")
          return True
        elif board[2][2]==board[1][2]==board[0][2]!=" ":
          print("The person who is: ",board[x][y],"wins")
          return True
        else:
          return False
def yatay():
  for i in range(3):
    for j in range(3):
      if board[i][j]==" ":
        if board[0][0]==board[0][1]==board[0][2]!=" ":
          print("The person who is: ",board[x][y],"wins")
          return True
        elif board[1][0]==board[1][1]==board[1][2]!=" ":
          print("The person who is: ",board[x][y],"wins")
          return True
        elif board[2][0]==board[2][1]==board[2][2]!=" ":
          print("The person who is: ",board[x][y],"wins")
          return True
        else:
          return False
def koyma(x,y,oyuncu):
  if board[x][y]==" ":
    board[x][y]=oyuncu
  else:
    print("Put the same spot! Put the same spot again and then it's your turn.")
def tahta():
  for i in range(3):
    for j in range(3):
      print(" I",board[i][j],end="")
    print(" I")
    print("--------------------------")
oyuncu="X"
def kazanma():
  if yatay() or dikey() or capraz():
    return True
  else:
    return False
while not kazanma():
  x=int(input())
  y=int(input())
  koyma(x,y,oyuncu)
  tahta()
  if oyuncu=="X":
    oyuncu="O"
  else:
    oyuncu="X"

