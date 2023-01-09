num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
a=num1
b=num2
while num1!=num2:
    if num1>num2:
      num1-=num2
    else:
        num2-=num1    
        print("hcf of",a,"add",b,"is",num1)
