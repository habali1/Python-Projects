#HISTOGRAM RANDOM BIG LIST in "x" axis.
import random
a = []
for i in range(100):
  n = random.randint(1,10)
  a.append(n)
print(a)
mx=[[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0]]
def counter(a):
  for i in a:
    if i == 1:
      mx[0][1]+=1
  for i in a:
    if i == 2:
      mx[1][1]+=1
  for i in a:
    if i == 3:
      mx[2][1]+=1
  for i in a:
    if i == 4:
      mx[3][1]+=1
  for i in a:
    if i == 5:
      mx[4][1]+=1
  for i in a:
    if i == 6:
      mx[5][1]+=1
  for i in a:
    if i == 7:
      mx[6][1]+=1
  for i in a:
    if i == 8:
      mx[7][1]+=1
  for i in a:
    if i == 9:
      mx[8][1]+=1
  for i in a:
    if i == 10:
      mx[9][1]+=1
  return mx
counter(a)
def mh(mx):
  print(str(1)+"  "+str("*"*mx[0][1]))
  print(str(2)+"  "+str("*"*mx[1][1]))
  print(str(3)+"  "+str("*"*mx[2][1]))
  print(str(4)+"  "+str("*"*mx[3][1]))
  print(str(5)+"  "+str("*"*mx[4][1]))
  print(str(6)+"  "+str("*"*mx[5][1]))
  print(str(7)+"  "+str("*"*mx[6][1]))
  print(str(8)+"  "+str("*"*mx[7][1]))
  print(str(9)+"  "+str("*"*mx[8][1]))
  print(str(10)+" "+str("*"*mx[9][1]))
mh(mx)
