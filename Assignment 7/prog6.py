s=input("enter a string")


match s:
    case s if ' ' in s:
        print("multiword string")
    case s if ' ' not in s:
        print("single word string")
            