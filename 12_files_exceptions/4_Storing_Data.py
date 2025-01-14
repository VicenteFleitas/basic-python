# 1. Using json.dumps() and json.loads()
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]
contents = json.dumps(numbers)
path = Path("data/numbers.json")
path.write_text(contents)

contents_json = path.read_text()
numbers2 = json.loads(contents_json)
print(numbers2)

# 2. Saving and Reading User-Generated Data
username = input("What is your name? ")
user_contents = json.dumps(username)
user_path = Path('data/username.json')
user_path.write_text(user_contents)
print(f"We'll remember you when you come back, {username}!")

path2 = Path('data/username.json')
contents2 = path2.read_text()
username2 = json.loads(contents2)
print(f"Welcome back, {username2}!")