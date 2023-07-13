#python program to create a class Rectangle with length and breadth
#inherit a class Box  with additional height and override method
class Rectangle:
    def __init__(self,l,b):
        self.length=1
        self.breadth=b
    def calc(self):
        area=self.length*self.breadth
        perim=2*(self.length*self.breadth)
        print('Area of rectangle='+str(area))
        print('Perimeter of rectangle='+str(perim))
class Box(Rectangle):
    def __init__(self, l, b, h):
        super().__init__(l, b)
        self.height=h
    def calc(self):
        volume=self.length*self.breadth*self.height
        print('volume of box='+str(volume))
x=input('enter the length of rectangle')
y=input('enter the breadth of rectangle')
l=int(x)
b=int(y)
r=Rectangle(l,b)
r.calc()
z=input('enter the height')
h=int(z)
b=Box(l,b,h)
b.calc()













    
    