import random
import os

clear = lambda: os.system('clear')

def game():
    score = 0
    pc_score = 0

    while True:
        game = ["rock", "paper", "scissors"]
        pc = random.choice(game)

        if score == 25:
            clear()
            print("You win!")
            exit()

        if pc_score == 25:
            clear()
            print("You lose!")
            exit()

        player = None

        while player not in game:
            player = input("rock, paper scissors?: ").lower()

            if player == "!commands":
                clear()
                print("!score --> YOUR SCORE")
                print("!exit --> EXIT")

            if player == "!score":
                clear()
                print("Your score: ",score)
                print("Pc score: ",pc_score)

            if player == "!exit":
                clear()
                print("OK!\n"
                      "BYE!")
                exit()

        if player == pc:
            clear()
            print(player, "VS", pc)
            print("Draw!")

            score = score + 1
            pc_score = pc_score + 1

        elif player == "rock":

            if pc == "paper":
                clear()
                print(player, "VS", pc)
                print("You lose!")

                score = score - 2
                pc_score = pc_score + 5

            if pc == "scissors":
                clear()
                print(player, "VS", pc)
                print("Youw win!")

                score = score + 5
                pc_score = pc_score - 2

        elif player == "paper":

            if pc == "rock":
                clear()
                print(player, "VS", pc)
                print("You win!")

                score = score + 5
                pc_score = pc_score - 2

            if pc == "scissors":
                clear()
                print(player, "VS", pc)
                print("Youw lose!")

                score = score - 2
                pc_score = pc_score + 5

        elif player == "scissors":

            if pc == "paper":
                clear()
                print(player, "VS", pc)
                print("You win!")

                score = score + 5
                pc_score = pc_score - 2

            if pc == "rock":
                clear()
                print(player, "VS", pc)
                print("Youw lose!")

                score = score - 2
                pc_score = pc_score + 5

def main():
    game()

if __name__ == '__main__':
    main()