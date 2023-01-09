n=int(input("enter a number:"))
s=''
while n:
    s=str(n%8)+s
    n=n//2
print(s)