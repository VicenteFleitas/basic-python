# 1. Handling the ZeroDivisionError Exception
# print(5/0)
# 1.1 Using try-except Blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!\n")

# 2. Using Exceptions to Prevent Crashes
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == "q":
#         break
#     second_number = input("Second number: ")
#     if second_number == "q":
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# 3. Handling the FileNotFoundError Exception
from pathlib import Path

# path = Path("text_files/alice.txt")
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")
# else:
#     # Count the approximate number of words in the file:
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file {path} has about {num_words} words.")

# 4. Working with Multiple Files
def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

# path = Path('text_files/alice.txts')
# count_words(path)

# 4.1 read with loop
filenames = ['alice.txt', 'Frankensteinn.txt', 'Dracula.txt']
for filename in filenames:
    path = Path(f"text_files/{filename}")
    count_words(path)

# 5 Failing Silently
try:
    print(alo)
except:
    pass