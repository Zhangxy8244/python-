import json

filename = 'my_username.json'
try:
    with open(filename) as file_object:
        r_username = json.load(file_object)
except FileNotFoundError:
    username = input("what's your name?")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("We'll remember you when you come back,"+username)
else:
    print("Welcome back,"+r_username)

