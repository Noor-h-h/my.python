import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "data.txt","w")

with open(file_path, "r", encoding="utf-8") as my_file:
    content = my_file.read()

print(content)
