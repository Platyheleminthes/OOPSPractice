"""
Inheritance Practice
"""
import numpy as np
class Shape:
    num_red = 0
    def __init__(self , color = "black"):
        self._color = color
        if self._color == "Red":
            Shape.num_red+=1
    def color(self):
        return self._color
    def set(self , newcolor):
        if self._color == "Red" and newcolor!="Red":
            Shape.num_red-=1
        elif newcolor =="Red" and self._color !="Red":
            Shape.num_red+=1
        else:
            pass
        self._color = newcolor
        return self
    
class Rectangle(Shape):
    def __init__(self , sidea, sideb, color = "black"):
        self.l = sidea
        self.b = sideb
        super().__init__(color=color)
    def area(self):
        return self.l*self.b

class Triangle(Shape):
    def __init__(self , base , height , color = "black"):
        self.b = base
        self.h = height
        super().__init__(color=color)
    def area(self):
        return 0.5*self.h*self.b

class Ellipse(Shape):
    def __init__(self , major_r  ,  minor_r,color = "black"):
        self.major_r = major_r
        self.minor_r = minor_r
        super().__init__(color=color)
    def area(self):
        return np.pi*self.major_r*self.minor_r

def turnred(shapeobject):
    if isinstance(shapeobject , Shape):
        shapeobject.set("Red")
        return shapeobject
    else:
        raise TypeError("input needs to be an instance of Class Shape")
    
class EquilateralTriangle(Triangle):
    def __init__(self , length , color = "black"):
        Triangle.__init__(self ,base=length , height=length*np.sqrt(3)/2 , color=color)

class Square(Rectangle):
    def __init__(self ,length , color = "black"):
        Rectangle.__init__(self ,sidea=length , sideb=length , color=color)

class Circle(Ellipse):
    def __init__(self ,length , color = "black"):
        Ellipse.__init__(self ,major_r=length,  minor_r=length , color=color)


