from pathlib import Path

# 1. Writing a Single Line
path = Path("text_files/programing.txt")
path.write_text("I love programing.")

# 2. Writing Multiple Lines
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)