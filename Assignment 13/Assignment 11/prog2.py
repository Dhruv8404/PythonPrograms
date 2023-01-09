from re import S


n=int(input("enter a nuber:"))
i=1
while i<=n:
    print(i,i**2)
    i+=1  
num=(n*(n+1)*(2*n+1))/6
print("sum=",num)