# Lists are ordered collections
friends = ["mabel", "dipper", "soos", "wendy", "stanley"]
print(friends)
print(friends[1])
print(friends[0].title())
print(friends[-1])

message = f"Hello {friends[0].title()}, how are you? This is {friends[-1].title()}"
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# motorcycles[2] = 'kawasaki'

motorcycles.append('kawasaki')
print(motorcycles)

series = []
series.append("breaking bad")
series.append("better call saul")
series.append("slam dunk")
series.append("berserk")
print(series)

series.insert(0, "dark")
print(series)

del series[3]
print(series)

last_serie = series.pop()
print(series)
print(f"The last serie that was ok: {last_serie.title()}")

series.remove("dark")
print(series)

# sort
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# temporal sort
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# reverse
cars.reverse()
print(cars)

# len
print(f"You have {len(cars)} cars.")

# loop
magicians = ['alice', 'david', 'carolina']
num = 0

for magician in magicians:
    num += 1
    print(f"Sos el numero: {num} Mago {magician.title()}")

print("Gracias a todos por el show!")

for value in range(1, 5):
    print(value)

lista_de_numeros = list(range(0, 5))
print(lista_de_numeros)

# lista num pares
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# el cuadrado
cuadrados = []
for valor in range(1, 11):
    cuadrado = valor ** 2
    cuadrados.append(cuadrado)

print(cuadrados)

# estadisticas
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# list comprehension
squares2 = [value**2 for value in range(1, 11)]
print(squares2)

# slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# players.sort()
print(players[0:3])
print(players[-3:])

# loop through slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# copy list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# tuple
dimensions = (1080, 720)
# print(dimensions[0])
# print(dimensions[1])
for dimension in dimensions:
    print(dimension)