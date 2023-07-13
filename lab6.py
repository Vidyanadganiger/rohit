#python program to demonstrate use of list compression
x=[10,11,12,13,17,18,20,22]
lsteven=[e for e in x if e%2==0]
lstsq=[i*i for i in range(1,10)]
s=input("enter the string with numbers")
l=s.split(' ')
noslst=[e for e in s if e.isdigit()]
print("original list"+str(x))
print("even number list"+str(lsteven))
print("squate of numbers from 1 to 9")
print(lstsq)
print("list creaed with numbers from string")
print(noslst)
