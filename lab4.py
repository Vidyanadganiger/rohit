#python program to find sun of digits of a number 
def sumofd(n):
    if(n==0):
        return 0
    else:
        return n%10+sumofd(n//10)
x=input("enter the number")
n=int(x)
total=sumofd(n)
print('sum of '+str(n)+"="+str(total))
