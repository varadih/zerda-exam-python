# Create a Rocket class.
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9".
# 2nd parameter: the starting fuel level as a number, defaults to 0.
# 3rd parameter: number of launches as a number, defaults to 0.

class Rocket():
    def __init__(self, rocket_type, fuel_level=0, launches=0):
        self.rocket_type = rocket_type
        self.fuel_level = fuel_level
        self.launches = launches

# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 fuels if it's a falcon9.
# it should increment the launches by one if it had enough fuel for the launch.
#
    def launch(self):
        if self.rocket_type == 'falcon1' and self.fuel_level >= 1:
            self.fuel_level -= 1
            self.launches += 1
        elif self.rocket_type == 'falcon9' and self.fuel_level >= 9:
            self.fuel_level -= 9
            self.launches += 1
        return "STAT AFTER LAUNCH:", {'launches':self.launches, 'fuel':self.fuel_level}

# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9.
# it should return the amount of fuel used for the refill.
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2.


    # def refill(self, rocket_type):
    #     if rocket_type == 'falcon1':
    #         return 'used fuel:', (5 - self.fuel_level)
    #         self.fuel_level == 5
    #
    #     elif rocket_type == 'falcon9':
    #         return 'used fuel:', (20 - self.fuel_level)
    #         self.fuel_level == 20

    def refill(self):
        if self.rocket_type == 'falcon1':
            used_fuel = 0
            while self.fuel_level < 5:
                self.fuel_level += 1
                used_fuel += 1
            return "USED FUEL IS:", (used_fuel)
        if self.rocket_type == 'falcon9':
            used_fuel = 0
            while self.fuel_level < 20:
                self.fuel_level += 1
                used_fuel += 1
            return "USED FUEL IS:", (used_fuel)

# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11, launches: 1"

    def getStats(self):
        return "STATISTIC:", {'name':self.rocket_type, 'fuel':self.fuel_level, 'launches':self.launches}

################################################

# nasa = Rocket('falcon9', 13)
# print(nasa.getStats())
# print(nasa.refill('falcon9'))
# print(nasa.launch('falcon9'))
# print(nasa.refill('falcon9'))
# print(nasa.getStats())
# print(nasa.launch('falcon9'))
# print(nasa.refill('falcon9'))
# print(nasa.getStats())



################################################

# The following code should work with the class:
#
falcon1 = Rocket('falcon1')
returned_falcon9 = Rocket('falcon9', 11, 1)

falcon1.refill() # 5
falcon1.launch()

print(falcon1.getStats()) # name: falcon1, fuel: 4, launches: 1
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11, launches: 1
