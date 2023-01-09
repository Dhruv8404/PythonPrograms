year=int(input("enter a number:"))




match (year):
        
    case year if year%50==0|year%4==0:
                print("century leap year")
    case year if year%4==0:
               print("non century leap year")
    
    
    case year if ():
        print("non century non leap year")
    case year if year%50==0:
        print("century non leap years")