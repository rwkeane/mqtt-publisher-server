import os

def parse(filepath : str):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Input file not found: {filepath}")

    username = None
    password = None

    with open(filepath, "r") as f:
        for line in f:
            key, value = line.strip().split("=", 1)
            if key == "username":
                username = value
            elif key == "password":
                password = value

    if username is None or password is None:
        raise ValueError("Invalid input file.")

    return username, password