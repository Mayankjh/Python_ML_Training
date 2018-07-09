#inheritance 
import time
class Vehicle:
    def general_usage(self):
        print("general usage : Transporation")
class Car(Vehicle):
        def __init__(self):
            print("I'am Car")
            self.wheeles = 4;
            self.has_roof = True
        def specific_usage(self):
            #self.general_usage()
            print("specific use: Commute to work, vacation with family")
class MotorCycle(Vehicle):
        def __init__(self):
            print("I'am Motorcycle")
            self.wheeles = 2
            self.has_roof = False
        def specific_usage(self):
            #self.general_usage()
            print("specific use: Road trip, Racing")
c = Car()
c.specific_usage()
c.general_usage()

time.sleep(1)
m = MotorCycle()
m.specific_usage()
m.general_usage()

print(isinstance(c,Vehicle)) 
print(isinstance(c,MotorCycle))
print(isinstance(m,Vehicle)) 
print(isinstance(m,MotorCycle))
print(isinstance(m,Car))
print(issubclass(Car,Vehicle))