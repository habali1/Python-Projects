#2048
#It is simple to play 2048 game that works with "left", "right", "up" and "down" commands.
import random

x=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]

#"2" sayısını %60, 4 sayısını %40 ihtimalle oluşturdum.
def r_num():
  t_f=[2,2,2,2,2,2,4,4,4,4]
  r=random.choice(t_f)
  b=random.randint(0,3)
  c=random.randint(0,3)
  if x[b][c]==0:
    x[b][c]=r
  else:
    r_num()
#Matrix'teki sayıları önce sola atıp sonra eşitlerse toplanmasını rightlayıp
#bir daha sola yapıştırdım bu işlemi tekrarlamamın sebebi 2,2,4,0 varken combo
#yapmamasını rightlamak yani 8,0,0,0 yapmamasını sağlamak
#Devamında da soluna altına ve upüne aynı işlemi yaptım.
def left():
     for m in range(4):
       for n in range(4):
         for l in range(3):
           if x[n][l]==0:
             x[n][l]=x[n][l+1]
             x[n][l+1]=0
     for i in range(4):
       for j in range(3):
         if x[i][j]==x[i][j+1]:
           x[i][j]= x[i][j]+x[i][j+1]
           x[i][j+1]=0
           if x[i][j]==2048:
            print("You win but Game is Not Over")
     for m in range(4):
       for n in range(4):
         for l in range(3):
           if x[n][l]==0:
             x[n][l]=x[n][l+1]
             x[n][l+1]=0


def right():
  for n in range(4):
    for i in range(4):
      for j in range(3,0,-1):
        if x[i][j]==0:
          x[i][j]=x[i][j-1]
          x[i][j-1]=0
  for i in range(4):
    for j in range(3,0,-1):
      if x[i][j]==x[i][j-1]:
        x[i][j]=x[i][j]+x[i][j-1]
        x[i][j-1]=0
        if x[i][j]==2048:
          print("You win but Game is Not Over")
  for n in range(4):
    for i in range(4):
      for j in range(3,0,-1):
        if x[i][j]==0:
          x[i][j]=x[i][j-1]
          x[i][j-1]=0

def up():
  for k in range(4):
    for i in range(4):
      for j in range(3):
        if x[j][i]==0:
          x[j][i]=x[j+1][i]
          x[j+1][i]=0
  for i in range(4):
    for j in range(3):
      if x[j][i]==x[j+1][i]:
        x[j][i]=x[j][i]+x[j+1][i]
        x[j+1][i]=0
        if x[j][i]==2048:
          print("You win and Game is Not Over")
  for k in range(4):
    for i in range(4):
      for j in range(3):
        if x[j][i]==0:
          x[j][i]=x[j+1][i]
          x[j+1][i]=0
def down():
  for k in range(4):
    for i in range(4):
      for j in range(3,0,-1):
        if x[j][i]==0:
          x[j][i]=x[j-1][i]
          x[j-1][i]=0
  for i in range(4):
    for j in range(3,0,-1):
      if x[j][i]==x[j-1][i]:
        x[j][i]=x[j][i]+x[j-1][i]
        x[j-1][i]=0
        if x[j][i]==2048:
          print("You win and Game is Not Over")
  for k in range(4):
    for i in range(4):
      for j in range(3,0,-1):
        if x[j][i]==0:
          x[j][i]=x[j-1][i]
          x[j-1][i]=0
#İki kere random sayıları atamasını rightladım çünkü oyun 2 tane random atanmış
#"2" veya "4" ile başlıyor
r_num()
r_num()
#Sonrasında matrisi gösterdim ki oyuncu tahtayı görüp yapacağı hamleyi düşünsün.
print(x[0])
print(x[1])
print(x[2])
print(x[3])
#Son olarak girdiği indislerle nereye kaydıracağını seçtirdim ve RecursionError
#alındığında oyunun bittiğini belirttim.
while True:
  xr=input()

  if xr=="left":
    left()
    try:
      r_num()
    except RecursionError:
      print("Game Over")
      break
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
  if xr=="right":
    right()
    try:
      r_num()
    except RecursionError:
      print("Game Over")
      break
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
  if xr=="up":
    up()
    try:
      r_num()
    except RecursionError:
      print("Game Over")
      break
    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])
  if xr=="down":
    down()
    try:
      r_num()
    except RecursionError:
      print("Game Over")
      break

    print(x[0])
    print(x[1])
    print(x[2])
    print(x[3])