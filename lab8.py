#python program to demonstrate any 5 operations on dictionary 
s="Microsoft is US based MNC Company Microsoft is working based on Cloud Computing"
d={}
lst=s.split(' ')
print('words in string')
print(lst)
for e in lst:
    if e in d:
        c=d.get(e)
        c=c+1
        d.update({e:c})
    else:
        d[e]=1
items=d.items()
print(items)
print('words in dictionary')
print(d.keys())
print('number of times appeared')
print(d.values())
