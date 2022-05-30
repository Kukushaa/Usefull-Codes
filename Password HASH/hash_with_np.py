#pip install numpy
import numpy as np
import random
import time
import os

clear = lambda: os.system('clear')

def hash(password):
    try:
        tmp = open('./hashed.txt', 'x')

    except FileExistsError:
        pass

    else:
        clear()
        print("We are creating a file, where will be saved your hashed password!")
        time.sleep(5)

        clear()
        time.sleep(1)


    for i in range(3):
        time.sleep(0.5)
        clear()

        print("Please wait, we are analizying your password.")
        time.sleep(0.5)
        clear()

        print("Please wait, we are analizying your password..")
        time.sleep(0.5)
        clear()

        print("Please wait, we are analizying your password...")
        time.sleep(0.5)
        clear()

        print("Please wait, we are analizying your password....")
        time.sleep(0.5)

    nums = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    symbols = np.array(("!", '@', "#", '$', "%",
               "&", "*", "?"))

    words = np.array(('q', 'w', 'e', 'r', 't', 'y',
             'u', 'i', 'o', 'p', 'a', 's',
             'd', 'f', 'g', 'h', 'j', 'k',
             'l', 'z', 'x', 'c', 'v', 'b',
             'n', 'm'))

    pass_len = len(password)
    hashed_tmp = ""

    for i in range(pass_len + random.choice(nums)):
        tmp_symbol = random.choice(symbols)
        tmp_word = random.choice(words)

        hashed_tmp = tmp_symbol + tmp_word + hashed_tmp

    copy = list(hashed_tmp)
    hashed_res = ""

    for i in copy:
        getter = random.choice(copy)

        hashed_res = getter + hashed_res

    clear()
    time.sleep(1)

    for i in range(8):
        time.sleep(0.5)
        clear()

        print("Please Wait, your password is Hashing! /")
        time.sleep(0.5)
        clear()

        print("Please Wait, your password is Hashing! |")
        time.sleep(0.5)
        clear()

        print("Please Wait, your password is Hashing! \ ")
        time.sleep(0.5)
        clear()

        print("Please Wait, your password is Hashing! -")
        time.sleep(0)

    clear()
    print(f"Password was hashed successfully: {hashed_res}")

    file = open("./hashed.txt", "a")
    file.write(f"{password} = {hashed_res}\n")
    file.close()

    return password

def main():
    password = input("Enter Your Password: ")
    hash(password)

if __name__ == '__main__':
    main()