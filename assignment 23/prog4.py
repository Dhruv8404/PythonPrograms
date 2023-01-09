def squre(n):
   x=1
   while n:
    yield x
    x+=1
    n-=1
for e in squre(int(input("enter a number:"))):
    print(e*e)        