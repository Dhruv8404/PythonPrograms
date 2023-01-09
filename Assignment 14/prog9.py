l = [1,2,3,5,5,4]
item_to_find = l

indices = [i for i in range(len(l)) if l[i] == item_to_find]
print(indices)
for i in range(len(l)):
    print(i)