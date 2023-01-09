import string
a=set("enter a character:")
def ispangram(string):
 
   return set(string.lower()) >= a
string=input("enter a string:")
if(ispangram(string) == True):
     print("yes")
else:
      print("no")   
 
