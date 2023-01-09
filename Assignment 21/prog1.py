def printn(n):
   if n>=0: 
    printn(n-1)
    print(n)
printn(int(input("enter a number:")))
    