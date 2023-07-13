#python program to write a function which take list as parameter 
def unique(l):
    lst=[]
    for e in l:
        if(l.count(e)==1):
            lst.append(e)
    return lst
l=[10,20,30,10,20,40,50,60]
lst=unique(l)
print(lst)
