upto=int(input("enter a number:"))

for num in range(2,upto+1):
    i=2
    for i in range(2,num):
     if num%i==0:
        i=num
        break;
    if i!=num:
        print(num,end=' ')