

def f1(n):
 while(n>0):
  
  temp=n
  rev=0   
  dig=n%10
  rev=rev*10+dig
  n=n/10
 if temp==rev:
     print("palidrome")
 else:
     print("non pelidrome")           
    
f1(437985)    