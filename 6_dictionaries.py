# A Simple Dictionary: 
# dictionary in Python is a collection of key-value (clave-valor) pairs
player = { 
    'name': 'dipper', 
    'age': 8, 
    'address': 'Gravity Falls',
    'friends': ['mabel', 'soos']
}
print(f"My name is {player['name']}, my friend is {player['friends'][0]}\n")

player['pos'] = {'x': 10, 'y': 12}
print(player)

# Starting with an Empty Dictionary
dog = {}
dog['age'] = 4
dog['color'] = 'white'
dog['name'] = 'snoopy'
dog['pos'] = 23
print(f"{dog}\n")

# use key to incrment values
car = { 'name': "audi", 'x_position': 0, 'y_position': 0, 'speed': 2 }
mov_in = 'y'
if mov_in == 'x':
    car['x_position'] += car['speed']
elif mov_in == 'y':
    car['y_position'] = car['y_position'] + car['speed']

print(f"{car['name']} goes {car['speed']} m/s x: {car['x_position']} y: {car['y_position']}")

# Removing Key-Value Pairs
planets = {'first': "mercury", 'second': "venus", 'third': "earth"}
del planets['first']
print(f"{planets}\n")

# A Dictionary of Similar Objects
people_fav_lang = {
    'mark': "javascript",
    'elon': "rust",
    'jeff': "python"
    }
fav_lang = people_fav_lang['jeff']
print(f"Jeff's favorite language is {fav_lang}\n")

# Using get() to Access Values
ship = {'name': "marry", 'color': "white", "speed": "9"}
print(ship.get('name'))
print(ship.get('age', "This key does't exist\n"))

# Looping Through All Key-Value Pairs from a list
user_0 = {
    'username': 'jhondoe99',
    'first': 'jhon',
    'last': 'doe',
}
# print(user_0.items())
for key, value in user_0.items():
    print(f"clave: {key}, valor: {value}\n")

fav_lang = {
    'mark': "javascript",
    'elon': "rust",
    'jeff': "python",
    'Nigel': "c",
    'Usop': "c",
    'sanji': "javascript",
}
print("\n")
for k, v in fav_lang.items():
    print(f"{k}'s favorite language is {v}\n")

# for name in fav_lang.keys():
for name in fav_lang:
    print(f"{name.title()}")

# list and dictionaries
friends = ["elon", "jeff"]

for name in fav_lang:
    print(f"Hi {name}")
    lang = fav_lang[name].title()
    if name in friends:
        print(f"{name} veo que te gusta {lang}")

# sorted()
for name in sorted(fav_lang.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print("\nThe following languages have been mentioned:")
for lang in fav_lang.values():
    print(lang.title())

# loop with no repetition using set
print("\n")
for lang in set(fav_lang.values()):
    print(f"fav lang: {lang}\n")

# Nesting pg: 105
# List of Dictionaries
alien_0 = { 'color': 'green', 'points':5 }
alien_1 = { 'color': 'yellow', 'points':10 }
alien_2 = { 'color': 'red', 'points':15 }

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print("...\n")

# list of aliens with range()
aliens = []
# make 30 aliens
for alien in range(30):
    new_alien = {'id': alien, 'color': "green", 'points': 5, 'speed': "slow"}
    aliens.append(new_alien)

# show first 5 aliens.
for alien in aliens[0:5]:
    print(alien)
print("...\n")

# show how many aliens have been created
print(f"total num of aliens: {len(aliens)}\n")

# A List in a Dictionary
# Store information about a pizza being ordered.
pizza = {
    'crust': "thick",
    'toppings': ["mushrooms", "extra cheese"]
}
# Summarize the order.
print(f"you ordered a {pizza['crust']} pizza. With the following toppings:")
for topping in pizza['toppings']:
    print(f"\n{topping}")
print("...\n")

# double for
programers = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'javascript'],
}

for name, langs in programers.items():
    if (len(langs) > 1):
        print(f"{name}'s fav langs are:")
        for lang in langs:
            print(lang)
    else:
        print(f"{name} fav lang is: {langs[0]}")

# A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': "albert",
        'last': "einstein",
        'location': "princeton",
    },
    'mcurie': {
        'first': "marie",
        'last': "curie",
        'location': "paris",
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

