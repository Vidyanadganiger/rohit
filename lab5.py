#python program to demonstrate 5 string operations
x=input("enter a string with extra spaces\n")
x=x.strip()
print("after removing spaces :"+x)
u=x.upper()
print("after converting to uppercase :"+u)
countd=0
counta=0
for c in x:
    if(c.isdigit()):
        countd=countd+1
    elif(c.isalpha()):
        counta=counta+1
print("number of digits="+str(countd))
print("number of alphabets"+str(counta))
words=x.split(' ')
print('after spliting into words')
print(words)
