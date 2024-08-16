#This is was the impossible task for me in the school nobody was capable of doing it.
#Task was removing same numbers with using only pop() method.
l=[1,2,3,4,4,10,10,10,10,4,4,4,4,5,6,7,8,9,9,9,9,9,9]
i=0
j=1
while i<(len(l)-2):
  while j<(len(l)-1):
    if l[i]==l[j]:
      if l[j]==l[len(l)-1]:
        try:
          while l[j]==l[len(l)-1]:
            l.pop()
          l[j],l[len(l)-1]=l[len(l)-1],l[j]
          l.pop()
        except IndexError:
          print(l)
      else:
        l[j],l[len(l)-1]=l[len(l)-1],l[j]
        l.pop()
    j+=1
  i+=1
  j=i+1
print(sorted(l))