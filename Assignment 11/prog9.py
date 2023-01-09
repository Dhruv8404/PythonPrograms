n=int(input("enter a number:"))
s=''
while n:
    s=str(n%2)+s
    n=n//2
print(s)