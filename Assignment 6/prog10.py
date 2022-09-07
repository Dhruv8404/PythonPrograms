x=int(input("enter 1st number:"))
y=int(input("enter 2nd  number:"))
z=int(input("enter 3rd  number:"))

if x>y and x>z:
    print("x is maximum")
elif y>x and y>z:
    print("y is a=maximum")
elif z>x and z>y:
    print("z is maximum")
else :
    print("error in entering a number")        