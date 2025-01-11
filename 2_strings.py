my_string = 'I told my friend, "Python is my favorite language!"'
print(my_string)

my_string = "The language 'Python' is named after Monty Python."
print(my_string)

my_string = "One of Python's strengths is its diverse and supportive community."
print(my_string)

name = "ADA lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# f: format
first_name = "ada"
last_name = "lovelace"
full_name = f"hello, {first_name} {last_name}!"
print(full_name)

# newline or tabs
print("python")
print("\tpython")
print("Languages:\nPython\nJavascript\nC")

print("Languages:\n\tPython\n\tJavascript\n\tC")

# Stripping Whitespace lstrip, rstrip, 'strip ambos lados'
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())

# removeprefix
url = "https://www.github.com/vicentefleitas"
url = url.removeprefix("https://")
print(url)