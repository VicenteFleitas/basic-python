# conditions
# action to take based on those conditions
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print(cars[1] == 'bmw')

promt = 'Audi'
if cars[0] == promt.lower():
    print(f"Found the {promt}!")

# inequality operator
if 'vicen' != 'vicen':
    print(f"not equal!")
else:
    print("equal!")

name1 = "vicen"
name2 = "david"

# and
if name1 == 'vicen' and name2 == 'david':
    print("both names are equal!")

# num
if 10 > 10:
    print("is bigger")
else:
    print("is smaller")

# or
resp1 = 28
resp2 = 25
if resp1 == 20 or resp2 == 25:
    print("you pass the test")

# Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('onions' in requested_toppings)

# Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expressions
game_active = True
can_edit = False

# Simple if Statements
music = False
if music:
    print("asi es!")

age = 19
if age >= 18:
    print("You are old enough to vote!\n")

# if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n")

# The if-elif-else Chain
# under age 4 is free.
# between the ages of 4 and 18 is $25.
# for anyone age 18 or older is $40.
person_age = 66

if person_age < 4:
    precio = 0
elif person_age < 18:
    precio = 25
elif person_age > 65:
    precio = 0
else:
    precio = 40
print(f"El costo seria: {precio}\n")

# Using if Statements with Lists
lista_coverturas = ['Champiñones', 'pimienta', 'queso', 'aceituna']

for covertura in lista_coverturas:
    if covertura == 'pimienta':
        print(f"Lo siento, ya no tenemos {covertura}")
    else:
        print(f"agregar {covertura}")
print("La pizza esta lista!\n".upper())

# check for empty list []
# lista_bebidas = ["coca", "pepsi", "guarana", "gulp"]
lista_bebidas = []

if lista_bebidas:
    for bebida in lista_bebidas:
        print(f"agregar {bebida}")
else:
    print("Favor seleccionar una bebida")

# Using Multiple Lists
lista_pedidos = ["coca", "pepsi", "guarana", "gulp"]
lista_disponible = ["coca", "pepsi", "guarana"]

for pedido in lista_pedidos:
    if pedido in lista_disponible:
        print(f"servir {pedido}")
    else:
        print(f"Lo siento, no tenemos {pedido}")
