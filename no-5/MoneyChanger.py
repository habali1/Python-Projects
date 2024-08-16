#Money Changer
#This function shows varieties of the amount that you type.
def changer(x):
  p=int(x)
  n=int(x/5)
  d=int(x/10)
  q=int(x/25)
  for i in range(p+1):
    for j in range(n+1):
      for k in range(d+1):
        for l in range(q+1):
          sum=i+j*5+k*10+l*25
          if sum==x:
            print("{} penny,{} nickel,{} dime,{} quarter".format(i,j,k,l))
  return
dollar = int(input("Enter the amount: "))
changer(dollar)