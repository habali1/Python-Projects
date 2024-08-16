#SHAKING LIST
#This code works by getting integers that you want to add and then it shakes the list where you want it to move and adds numbers side by side.
def shake_list():

  shake_list=[]
  while True:
    inp=int(input("Enter: "))
    shake_list.append(inp)
    if len(shake_list)==10:
      break
    if inp==0:
      break

  while len(shake_list)!=1:
    l=len(shake_list)
    inp1=input("Enter R or L: ")
    if inp1=='R':
      new_elem=shake_list[l-2]+shake_list[l-1]
      shake_list[l-2]=new_elem
      shake_list.remove(shake_list[l-1])
      print(shake_list)
    elif inp1=='L':
      new_elem=shake_list[0]+shake_list[1]
      shake_list[1]=new_elem
      shake_list.remove(shake_list[0])
      print(shake_list)
    elif inp1=='X':
      break

shake_list()