class Engine:
    def __init__(self , type = "Not Specified"):
        self.type = type
    def start(self):
        print("Petrol engine starting...")

class Car:
    def __init__(self ,engine):
        self.objeng = engine
    def start(self):
        self.objeng.start()
        print("Car started.") 
class Transmission:
    def __init__(self , type = "Not Specified" , ngears = 5):
        self.type = type
        self.ngears = ngears
        self.gear = 0
    def type(self):
        return self.type
    def gear(self):
        return self.gear
    def shift_up(self):
        if self.gear ==5:
            raise Exception("Can't go beyond the maximum limit")
        elif self.type =="automatic":
            raise RuntimeError("Cannot manually shift gears in with an automatic transmission.")
        else:
            self.gear+=1
    def shift_down(self):
        if self.gear ==0:
            raise Exception("Can't go below the minimum limit")
        elif self.type =="automatic":
            raise RuntimeError("Cannot manually shift gears in with an automatic transmission.")
        else:
            self.gear-=1
        
    