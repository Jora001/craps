import random


def roll_dice():
    dice = [random.randint(1, 6), random.randint(1, 6)]
    total = dice[0] + dice[1]

    print(f"The sum of dice is {dice[0]} + {dice[1]} = {total}")

    return total


def play_craps():
    first_roll = roll_dice()

    win_numbers = [7, 11]
    lose_numbers = [2, 3, 12]

    if first_roll in win_numbers:
        print("You won")

    elif first_roll in lose_numbers:
        print("You lose")

    else:
        goal = first_roll

        print(f"Now your goal number is {goal}")

        while True:
            current_roll = roll_dice()

            if current_roll == goal:
                print("You won")
                break

            elif current_roll == 7:
                print("You lose")
                break


play_craps()