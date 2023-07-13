#python program to find the sum of elements using recursion
def lstsum(l ,n):
    if(n==0):
        return l[0]
    else:
        return l[n]+lstsum(l,n-1)  
l=[10,20,30,40]
n=len(l)-1
total=lstsum(l,n)
print("total of al elements ="+str(total))
