


def odd(n):
   x=1
   while n:
    yield x
    x+=2
    n-=1
for e in odd(int(input("enter a number:"))):
    print(e)        