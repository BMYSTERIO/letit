def get_username():
    with open("data/username.txt", "r") as file:
        lines = file.readlines()
        if lines:
            return lines[0]

def save_usrname(username):
    with open("data/username.txt", "r") as file:
        lines = file.readlines()
    with open("data/username.txt", "w") as file:
        if lines:
            lines[0] = username
            file.write(lines[0])