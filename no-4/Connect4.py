#CONNECT4
#It is easy to play connect4 game 0: empty , 1: red, 2: yellow
#It starts from 1 to 7 so wherever you want to place your disc you just type it
#and at the bottom you see that it is placed at the location that you want.

#0= boş 1= kırmızı 2= sarı
#Tahtayı yaratıp tüm kazanma ihtimallerini oluşturdum.
#Dikey, yatay ve çapraz olarak 4 tane pulun ardaşık olarak yan yana
#geldiği seneryoları düşünüp kazanan tüm durumları belirledim.
b=[[0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0]]
def tahta():
  for i in range(6):
    for j in range(7):
      print(b[i][j],end="")
    print(" ")
def yatay():
  for i in range(6):
    for j in range(4):
      if b[i][j]!=0:
        if b[i][j]==b[i][j+1]==b[i][j+2]==b[i][j+3]:
          print("Oyuncu",b[i][j],"Kazandı")
          return True
  return False
def dikey():
  for i in range(3):
    for j in range(6):
      if b[i][j]!=0:
        if b[i][j]==b[i+1][j]==b[i+2][j]==b[i+3][j]:
          print("Oyuncu",b[i][j],"Kazandı")
          return True
  return False
def çapraz():
  for i in range(3,6):
    for j in range(0,4):
      if b[i][j]!=0:
        if b[i][j]==b[i-1][j+1]==b[i-2][j+2]==b[i-3][j+3]:
          print("Oyuncu",b[i][j],"Kazandı")
          return True
  for i in range(0,3):
    for j in range(0,4):
      if b[i][j]!=0:
        if b[i][j]==b[i+1][j+1]==b[i+2][j+2]==b[i+3][j+3]:
          print("Player", b[i][j],"Kazandı")
          return True
  return False
#Her oyuncunun sıra sıra dikey bir şekilde pulları atabilmeleri için
#dikey hizalayıp atmalarını sağladım.
#Her atıştan sonra oyuncunun değişmesini "1" ve "2" sayılarıyla sağladım.
#"1" kırmızıyı "2" de sarıyı belirtiyor. Aynı zamanda 1. ve 2. oyuncuyu.
#For loopuyla oyunu alttan başlattım gerçek hayatta olduğu gibi.
def atış(j, oyuncu):
  j-=1
  for i in range(5,-1,-1):
    if b[i][j]==0:
      b[i][j]=oyuncu
      break
oyuncu=1
#Kazanananı belirlemek adına while döngüsü kurdum ve gereken koşullar
#sağlandığında "True" döndürüp bitmesini sağladım.
def kazanma():
  if yatay() or dikey() or çapraz():
    return True
  else:
    return False
while not kazanma():
  j=int(input())
  atış(j,oyuncu)
  tahta()
  if oyuncu==1:
    oyuncu=2
  else:
    oyuncu=1