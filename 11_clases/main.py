# Class names should be written in CamelCase

from dog import Dog
from car import Car
from electric_car import ElectricCar

# 1. create a instance
my_dog = Dog('willie', 6)

print(f"My dogs name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

# 2. Creating Multiple Instances

# 3. car
my_new_car = Car("audi", "a4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an Attribute’s Value Through a Method
my_new_car.update_odometer(33)
my_new_car.read_odometer()

# no one tries to roll back the odometer reading
my_new_car.update_odometer(31)

# Incrementing an Attribute’s Value Through a Method
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# Inheritance
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Defining Attributes and Methods for the Child Class
# my_leaf.describe_battery()

# Overriding Methods from the Parent Class
my_used_car.fill_car(10)
my_leaf.fill_car(10)

# composition: Instances as Attributes
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()



