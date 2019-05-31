# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class
class Vehicle:
    def __init__(self, name):
        pass

# Subclass
class FlightVehicle(Vehicle):
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        pass

class Starship(FlightVehicle):
    def __init__(self):
        return super().__init__(name="Millinial Falcon")

# Subclass
class GroundVehicle(Vehicle):
    def __init__(self):
        pass

class Car(GroundVehicle):
    def __init__(self):
        return super().__init__(name="Mustang")

class Motorcycle(GroundVehicle):
    def __init__(self):
        return super().__init__(name="Yamaha")
