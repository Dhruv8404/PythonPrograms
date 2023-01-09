upto=100

for num in range(2,upto):
    i=2
    for i in range(2,num):
     if num%i==0:
        i=num
        break;
    if i!=num:
        print(num,end=' ')