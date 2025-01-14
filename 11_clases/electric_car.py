from car import Car
from battery import Battery

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # self.battery_size = 40
        self.battery = Battery()

    # def describe_battery(self):
    #     """Print a statement describing the battery size"""
    #     print(f"This car has a {self.battery_size}-KWh battery.")

    def fill_car(self, amount):
        """pass amount o KW to charge the battery"""
        print(f"You charge {amount}% of the battery.")