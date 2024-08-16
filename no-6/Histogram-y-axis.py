#HISTOGRAM BIG RANDOM LIST in "y" axis.
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
    max_count = max([i[1] for i in mx])
    for count in range(max_count, 0, -1):
        row = ''
        for i in mx:
            if i[1] >= count:
                row += '*  '
            else:
                row += '   '
        print(row)
    row = ''
    for i in mx:
        row += str(i[0]) + '  '
    print(row)

mh(mx)
