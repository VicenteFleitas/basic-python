# define function with def
# describes the func with "docstring," enclosed in triple quotes,
def greet_user():
    """Display a simple greeting"""
    print("hello")

greet_user()

# Passing Information to a Function, username its the param
def greet_by_name(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")
# "vicen" its the argument
greet_by_name("Vicen")

# Arguments and Parameters
# 1. Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display info about pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}")

describe_pet('hamster', 'harry')
#Multiple Function Calls
describe_pet('dog', 'willie')
#Order Matters in Positional Arguments

# 2. Keyword Arguments
describe_pet(pet_name='lars', animal_type='bird')

# Default Values
def describe_pet2(petName, animalType='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animalType}.")
    print(f"My {animalType}'s name is {petName.title()}.")

describe_pet2("Amigo")

# Return Values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"\n{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)
print(get_formatted_name("steve", "vai"))

# Making an Argument Optional
def get_formatted_name2(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name2("Steve", "Ray"))

# Returning a Dictionary
# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person

# print(build_person("vicen", "fleitas"))

def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

print(build_person("vicen", "fleitas", 25))

# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
print("\n")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# now with func
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    return completed_models

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

final = print_models(["new design", "old design"], [])
show_completed_models(final)

# Preventing a Function from Modifying a List
weekly_task = ["clean", "feed animals", "home work"]
print_models(weekly_task[:],[])
print(weekly_task)

# 1. Passing an Arbitrary Number of Arguments
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(f"\n{toppings}")

# make_pizza("queso")
# make_pizza("queso", "peperoni")

# 1.1. Now we can replace the print() call with a loop
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    for topping in toppings:
        print(f"- {topping}")
print("\n")
make_pizza("queso")
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments