l1=[1,2,"hello",3,"true"]
for i in l1:
    if(type(i)!=int):
        l1.remove(i)
print(l1)        