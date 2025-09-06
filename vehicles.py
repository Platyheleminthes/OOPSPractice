class Engine:
    def __init__(self , type = "Not Specified"):
        self.type = type
    def start(self):
        print("Petrol engine starting...")

class Car:
    def __init__(self ,engine , transmission):
        self.engine = engine
        self.transmission = transmission
    def start(self):
        if self.transmission.gear!=0 and self.transmission.type == "manual":
            raise RuntimeError("It is unsafe to start the car while in gear")
        self.engine.start()
        print("Car started.")
    def acc_shift_up(self):
        self.transmission.shift_up()
    def acc_shift_down(self):
        self.transmission.shift_down() 
class Transmission:
    def __init__(self , type = "Not Specified" , ngears = 5):
        self.type = type
        self.ngears = ngears
        self.gear = 0
    def acc_type(self):
        return self.type
    def acc_gear(self):
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
        
    