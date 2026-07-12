class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []

vehicle = Vehicle(20)
print(vehicle.max_speed)
print(vehicle.mileage)
print(vehicle.gadgets)
vehicle.gadgets.append("GPS")
print(vehicle.gadgets)