l=[1,1,1,2,3,4,7,5,3,2,3,5]
freq={}
for element in l:
    freq[element]=l.count(element)
for k,v in freq.items():
    print(k,v)