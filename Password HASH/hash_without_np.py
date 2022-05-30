import random
import time
import os

clear = lambda: os.system('clear')

def hash(password):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    symbols = ["!", '@', "#", '$', "%",
               "&", "*", "?"]

    words = ['q', 'w', 'e', 'r', 't', 'y',
             'u', 'i', 'o', 'p', 'a', 's',
             'd', 'f', 'g', 'h', 'j', 'k',
             'l', 'z', 'x', 'c', 'v', 'b',
             'n', 'm']

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
    print(f"Password hashed successfully: {hashed_res}")

    return password

def main():
    password = input("Enter Your Password: ").lower()
    hash(password)

if __name__ == '__main__':
    main()