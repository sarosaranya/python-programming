num=input("enter the number")
temp=num
sum=0
while temp>0:
    x=temp%10
    sum+=x**3
    temp//=10
if(num==sum):
    print(" yes it is an armstrong number")
else:
    print("no it is not an armstrong number")
    
