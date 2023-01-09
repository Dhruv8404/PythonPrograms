start=int(input("enter inclusive value:"))
end=int(input("enter a number:"))

for num in range(start,end):
    i=2
    for i in range(start,num):
     if num%i==0:
        i=num
        break;
    if i!=num:
        print(num,end=' ')

