# The Python Standard Library
# You can use any function or class in the standard library by
# including a simple import statement at the top of your file.
# A. random module
from random import randint, choice

# 1. randint
random_int = randint(1, 6)
print(random_int)

# 2. choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(f"\n{first_up}")