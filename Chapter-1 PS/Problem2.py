import os

# Specify the directory path
directory_path = "Happy"

try:
    # List contents of the directory
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
