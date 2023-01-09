def squre(n):
   if n>=0: 
    squre(n-1)
    print(n*n)
squre(int(input("enter a number:")))
    