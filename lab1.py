#python program to find factorial of a number 
def fact(n):
    f=1
    i=1
    while(i<=n):
        f=f*i 
        i=i+1
    print("The factorial of "+str(n)+"="+str(f))
x=input("enter the number")
n=int(x)
fact(n)
