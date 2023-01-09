def even(n):
   x=2
   while n:
    yield x
    x+=2
    n-=1
for e in even(int(input("enter a number:"))):
    print(e)        