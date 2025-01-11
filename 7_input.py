# import sys
# print (sys.argv[1])
message = input("Tell me something and i will repeat: ")
print(f"your message is: {message}\n")


prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# Using int() to Accept Numerical Input
# test on cmd and then use age to see the real value
age = input("How old are you? ")
age = int(age)
if age > 21:
    print("you are older\n")

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# The Modulo Operator
print(f"4 % 3: {4 % 3}")
print(f"7 % 3: {7 % 3}")

# even odd game
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"the number {number} is even")
else:
    print(f"the number {number} is odd")