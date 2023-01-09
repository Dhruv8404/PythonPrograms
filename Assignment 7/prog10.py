from calendar import c
from re import A


s1=input("enter a colour:")
l1=["yellow","blue","orenge","white","black","red"]
for e in l1:
 if e in s1:
    break
      
 else:
    e="other"  
match e:
    case "yellow":
        print("monday")
    case "blue":
        print("tusday")
    case "orenge":
        print("wednesday")
    case "white":
        print("thrusday")
    case "black":
        print("friday")
    case "red":
        print("saturday")
    case "other":
        print("sunday")            
                    