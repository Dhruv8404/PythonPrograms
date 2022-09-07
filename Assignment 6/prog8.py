

x=int(input("enter 1st quadratic number:"))
Y=int(input("enter 2nd quadratic number:"))
z=int(input("enter 3rd quadratic number:"))
d=Y**2-4*x*z
if d>0:
    print("real distinct")
elif d<0:
    print("inaginary roor")
else :
    print("real equal")
