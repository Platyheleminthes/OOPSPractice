"""
Inheritance Practice
"""
import numpy as np
class Shape:
    def __init__(self , color = "black"):
        self._color = color
    def color(self):
        return self._color
    def set(self , newcolor):
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
        return 0.5*self.l*self.b

class Ellipse(Shape):
    def __init__(self , major_r  ,  minor_r,color = "black"):
        self.major_r = major_r
        self.minor_r = minor_r
        super().__init__(color=color)
    def area(self):
        return np.pi*self.major_r*self.minor_r

def turnred(shapeobject):
    if isinstance(shapeobject , Shape):
        shapeobject._color = "Red"
        return shapeobject
    else:
        raise TypeError("input needs to be an instance of Class Shape")
    
