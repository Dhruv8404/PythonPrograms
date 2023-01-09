s1=input("enter a string")
s2=input("enter a string")

match (s1,s2):
    case (s1,s2) if s1==s2:
        print("equal")
    case (s1,s2) if s1>s2:
        print("s1 is grater") 
    case(s1,s2) if s2>s1:
        print("s2 is grater")    
            