s=int(input("enter a number"))

match s:
    case s if s>0  :
        print("positive")
    case s  if s<0  :
        print("negative")
    case s if s==0 :
        print("zero")       