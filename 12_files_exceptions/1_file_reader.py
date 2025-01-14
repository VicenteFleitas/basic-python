from pathlib import Path

# A. Reading the Contents of a File
path = Path('text_files/pi_digits.txt')
contents = path.read_text()
# contents = contents.rstrip()
print(contents)

# Relative and Absolute File Paths
# 1. relative
path2 = Path('text_files/filename.txt') 
contents2 = path2.read_text().rstrip()
print(f"\n{contents2}\n\n")
# 2. absolute
# path = Path('/Documents/project2024/python/12_files_exceptions/text_files/filename.txt')

# B. Accessing a File’s Lines
lines = contents.splitlines()
for line in lines:
    print(f"\n{line}")

# 1. Working with a File’s Contents
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))

# 2. Large Files: One Million Digits
path3 = Path("text_files/pi_million_digits.txt")
content3 = path3.read_text()
lines3 = content3.splitlines()

pi_string3 = ""
for line in lines3:
    pi_string3 += line.lstrip()
print(f"\n{pi_string3[:52]}...")
print(len(pi_string3))

# Is Your Birthday Contained in Pi?
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string3:
    print("Your birthday apperas in the first million digits of pi!")
else:
    print("bad luck.")