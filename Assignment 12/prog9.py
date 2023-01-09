a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
if a>b:
    min=a
else:
    min=b
while(1):
    if(min%a==0 and min%b==0):
        print("lcm is=",min)
        break
    min=min+1        
