import string
import random
import os

clear = lambda: os.system('clear')

def generate_random_password(name, length):
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    if length < 5:
        clear()
        print("Password length is TOO SMALL!")
        exit()

    elif length > 20:
        clear()
        print("Password length is TOO BIG!")
        exit()

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    clear()
    return f"Your RD Password is: \n" \
           f"{name.capitalize() + ''.join(password)}"

def main():
    name = input("Enter your name: ")
    try:
        length = int(input("Enter PASSWORD length: "))
    except ValueError:
        print(f"Sorry, but enter only NUMS\n"
              "Not {length}")
    else:
        print(generate_random_password(name, length))

if __name__ == '__main__':
    main()