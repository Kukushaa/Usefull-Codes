import os

clear = lambda: os.system('clear')

def finder(car):
    clear()
    try:
        f = open("./car.txt", "r")
    except FileNotFoundError:
        clear()
        print("Sorry! But this file is DELETED!")
        exit()
    else:
        pass

    i = 1
    line = ""

    while i > 0:
        tmp = f.readline()

        if i > 10:
            clear()

            print(f"Sorry, but I cant find your {car} :(")
            print(f"Please check if your {car} is correctly written <3")

            exit()

        elif car not in tmp:
            i += 1

        else:
            line = tmp
            i = 0

    contry = line.index(":")
    country = line[:contry]

    clear()
    print(f"Your {car} is from: {country}")

def main():
    clear()
    car = input("Enter your car: ").capitalize()
    if car in "Japan":
        print("Ha-Ha :D\n"
              "Very funny")
    elif car in "Germany":
        print("Ha-Ha :D\n"
              "Very funny")
    else:
        finder(car)

if __name__ == '__main__':
    main()