from difflib import Match


print("enter length of triangle in sequence")
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))

print("menu")
print("press 1 if you want to check isosceles triangle ")
print("press 2 if you want to check  length of sides of a right angle triangle")
print("press 3 if you want to check equilateral  triangle")

 
 
if (a==b) | (a==c) | (b==c):
    print("isosolus triangle")
else:
    print("not isosolus triangle ")    
    