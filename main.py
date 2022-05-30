import time
import os

clear = lambda: os.system("clear")

def main():
    for i in range(15):
        clear()
        print("Loading.")
        time.sleep(0.5)
        clear()
        print("Loading..")
        time.sleep(0.5)
        clear()
        print("Loading...")
        time.sleep(0.5)
        clear()
        print("Loading....")
        time.sleep(0.5)
    print("Hi :)")

if __name__ == '__main__':
    main()