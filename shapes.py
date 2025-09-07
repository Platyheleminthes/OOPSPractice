"""
Inheritance Practice
"""

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
        
