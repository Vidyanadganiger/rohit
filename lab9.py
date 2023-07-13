#python program to import calculation.py module
import calculation as c
x=input("enter the first no")
y=input("enter the second no")
a=int(x)
b=int(y)
result=c.add(a,b)
print('addition of '+str(a)+'and'+str(b)+'='+str(result))
result=c.sub(a,b)
print('subtraction of '+str(a)+'and'+str(b)+'='+str(result))
result=c.multiply(a,b)
print('multiplication of '+str(a)+'and'+str(b)+'='+str(result))
result=c.divide(a,b)
print('division of '+str(a)+'and'+str(b)+'='+str(result))
