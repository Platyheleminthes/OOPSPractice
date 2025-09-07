""""""
import numpy as np
from shapes import *

class RegularPolygon(Shape):
    def __init__(self , n_sides, side_length, color = "black"):
        self.n_sides = n_sides
        self.side_length = side_length
        Shape.__init__(self , color=color)
    def areas(self):
        return (((self.side_length)**2)/4)/(np.tan(np.pi/self.n_sides))
    def interior_angle(self):
        return 180*(self.n_sides-2)/(self.n_sides)
    def can_tessellate(self):
        if 360% self.interior_angle()==0:
            return True
        else:
            return False
class EquilateralTriangle(RegularPolygon):
    def __init__(self , side_length , color = "black"):
        RegularPolygon.__init__(self , n_sides=3 , side_length=side_length , color=color)

class Square(RegularPolygon):
    def __init__(self , side_length , color = "black"):
        RegularPolygon.__init__(self , n_sides=4 , side_length=side_length , color=color)

class Pentagon(RegularPolygon):
    def __init__(self , side_length , color = "black"):
        RegularPolygon.__init__(self , n_sides=5 , side_length=side_length , color=color)
    