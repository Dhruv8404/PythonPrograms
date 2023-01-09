def cube(n):
   if n>=0: 
    cube(n-1)
    print(n*n*n)
cube(int(input("enter a number:")))
    