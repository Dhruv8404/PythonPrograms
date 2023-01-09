def printn(n):
    if n>0:
     print(n)
     printn(n-1)
    
printn(int(input("enter a number:")))    