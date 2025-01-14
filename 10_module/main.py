# 1. import all from module
# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 2. Importing Specific Functions
# from pizza import make_pizza, client_list

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# client_list(["vicen", "Gio", "Deisy"])


# 3. Using as to Give a Function an Alias
# from pizza import make_pizza as mp

# mp(8, "queso", "peperoni", "borde relleno")


# 4. Using as to Give a Module an Alias
# import pizza as p

# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 5. Importing All Functions in a Module
from pizza import *

client_list(["vicen"])