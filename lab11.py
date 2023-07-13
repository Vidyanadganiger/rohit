#python program to create a class circle and radius and calculate area and parameter of circle
class Circle:
    def __init__(self,r):
        self.radius=r
    def calc1(self):
        area=3.142*self.radius*self.radius
        print("area of circle="+str(area))
    def calc2(self):
        perimeter=2*3.142*self.radius
        print("perimeter of cirlce="+str(perimeter))
x=input('enter the radius')
r=int(x)
c=Circle(r)
c.calc1()
c.calc2()