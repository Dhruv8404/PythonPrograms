def printn(n):
   if n>0:
    print(n*2) 
    printn(n-1)

printn(int(input("enter a number:")))