a=input("enter the number")
b=input("enter the number")
for i in range(a,b+1):
  if i>1:
    for num in range(2,i):
      if(i%num)==0:
        break
    else:
      print(i)
    
